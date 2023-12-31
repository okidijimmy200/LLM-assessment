import io, logfile
import pandas as pd
from utils.utils import clean_and_process_string
from models.models import (
    DocRequest,
    DocResponse,
    VectorStoreRequest,
    QueryRequest,
    QueryResponse,
)
from service.interface import IDocumentQAService, ICleanStoreService, IVectorStore
from langchain.llms import DeepInfra
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.prompts import (
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
    ChatPromptTemplate,
)


class CleanStoreService(ICleanStoreService):
    """Service to clean and store csv file to be processed"""

    def __init__(self) -> None:
        self.logging = logfile.get_logger()

    def clean_store_csv(self, req: DocRequest) -> DocResponse:
        try:
            df = pd.read_csv(io.BytesIO(req.file.read()))

            numeric_values = pd.to_numeric(
                df["text"]
                .replace({",": ""}, regex=True)
                .replace("[^a-zA-Z0-9]", "0", regex=True),
                errors="coerce",
            )

            df.drop(df[numeric_values.notna()].index, inplace=True)

            df.to_csv(f"documents/{req.file.filename}", index=False)

            return DocResponse(
                200, "Document Successfully stored", f"{req.file.filename}"
            )

        except Exception as e:
            self.logging.error(f"-Error " + f"{type(e).__name__} {str(e)}")
            return DocResponse(500, "Internal Server Error")


class DocumentQAService(IDocumentQAService):
    """Question and Answer Service. For now, this is specific to segments.csv file, but adjustments can me made to accomade different files"""

    storage: IVectorStore

    def __init__(self, storage: IVectorStore) -> None:
        self.storage = storage
        self.logging = logfile.get_logger()


    def question_answer(self, req: QueryRequest) -> QueryResponse:
        try:
            print(req.query, 'query')
            llm = DeepInfra(model_id="meta-llama/Llama-2-70b-chat-hf")
            llm.model_kwargs = {
                "temperature": 0.7,
                "repetition_penalty": 1.2,
                "max_new_tokens": 250,
                "top_p": 0.9,
            }
            loader = CSVLoader(
                file_path=f"documents/text_segments.csv",
                encoding="utf-8",
                csv_args={
                    "delimiter": ",",
                    "quotechar": '"',
                    "fieldnames": ["text", "pagenum", "doc_name"],
                },
            )
            data = loader.load()

            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=500, chunk_overlap=20
            )
            text_chunks = text_splitter.split_documents(data)

            store_res = self.storage.vector_store(
                VectorStoreRequest(text_chunks)
            )

            system_template = """The provided {context} is a tabular dataset containing text, pagenum and doc_names columns.
                            Note: When asked a question, try to generate response information with basis from the provided context then maybe add 
                            other sources if need be. Make it simple and clear. If you are not sure of the answer, just say you donot know.
                            
                ----------------
                {context}"""

            # Create the chat prompt templates
            messages = [
                SystemMessagePromptTemplate.from_template(system_template),
                HumanMessagePromptTemplate.from_template("{question}"),
            ]

            qa_prompt = ChatPromptTemplate.from_messages(messages)
            memory = ConversationBufferMemory(
                memory_key="chat_history", output_key="answer", return_messages=True
            )
            qa = ConversationalRetrievalChain.from_llm(
                llm,
                retriever=store_res.response.as_retriever(search_kwargs={"k": 20}),
                return_source_documents=False,
                combine_docs_chain_kwargs={"prompt": qa_prompt},
                memory=memory,
                verbose=True,
            )
            res = qa.run({"question": f"{req.query}"})
            return QueryResponse(200, clean_and_process_string(res))
        except Exception as e:
            self.logging.error(f"error: " + f"{type(e).__name__} {str(e)}")
            return QueryResponse(500, "Internal Server Error")
