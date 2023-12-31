import logfile
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from models.models import (
    VectorStoreRequest,
    VectorStoreResponse,
)
from service.interface import IVectorStore
from config.config import Config


class VectorStore(IVectorStore):
    config: Config

    def __init__(self, config: Config) -> None:
        self.config = config
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            model_kwargs={"device": "cpu"},
        )
        self.logging = logfile.get_logger()

    def vector_store(self, req: VectorStoreRequest) -> VectorStoreResponse:
        try:
            db = FAISS.from_documents(req.chunks, self.embeddings)
            db.save_local(self.config.db_faiss_path)
            return VectorStoreResponse(200, db)
        except Exception as e:
            self.logging.error(
                f"Error storing vectors: " + f"{type(e).__name__} {str(e)}"
            )
            return VectorStoreResponse(500, "Internal server error")
