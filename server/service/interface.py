from abc import ABC, abstractmethod
from models.models import (
    DocRequest,
    DocResponse,
    VectorStoreRequest,
    VectorStoreResponse,
    QueryRequest,
    QueryResponse,
)


class ICleanStoreService(ABC):
    @abstractmethod
    def clean_store_csv(self, req: DocRequest) -> DocResponse:
        pass


class IDocumentQAService(ABC):
    @abstractmethod
    def question_answer(self, req: QueryRequest) -> QueryResponse:
        pass


class IVectorStore(ABC):
    @abstractmethod
    def vector_store(self, req: VectorStoreRequest) -> VectorStoreResponse:
        pass
