Backend for Question and Answering of Documents using LLMs.

Data Engineering:
The text_segments.csv file contains three columns i.e text, pagenum and doc_name.
The text column contains multiple rows with text strings, numbers, alphanumeric values and signs.
Since this column is all about text, i dropped columns containing only numbers, alphanumeric values leaving only text. This is done using pandas library and the contents later saved in documents folder ready to be queried.

API Endpoints:
1. /api/vi/document/upload-csv 
method: POST
params: {"csv": csv}
This endpoint is ended to upload the csv file, perform cleaning and later store the file in the documents folder.

2. /api/vi/document/query-document
method: POST
params: {"query": query}
This endpoint is intended to perform query on the csv file by first uploading the file using CSVLoader from langchain library.
We later perform text character splitting and use huggingface sentence-transformer model to create embeddings which we then store to a vector database called Faiss.

We use deepinfra using meta-llama/Llama-2-70b-chat-hf model to run the query and return the desired response by ranking the most close vectors
The response is cleaned and a string is returned

Challenges:
1. The sentence-transformer library is really big in size and takes a long time to download and execute
2. Creating a dockerfile using pytorch image is also big taking a long installation and run time.
3. The LLM sometimes doesnot produce correct responses as intended by the query.
4. It generally takes a long time to execute a query because of the large files that have to be run
5. Automatic installations everytime we run the server, which slows the runtime of the application

Improvements:
1. Try a different embeddings model that is faster, probably one hosted online e.g OpenAI embedding models
2. Try a gpt-4 LLM to produce better responses from the query made.
3. Probably use csv-agents for csv documents
4. Write unittests 
