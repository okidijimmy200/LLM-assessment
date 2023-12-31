from dataclasses import dataclass
from typing import Optional


@dataclass
class DocRequest:
    file: bytes


@dataclass
class DocResponse:
    code: int
    detail: str
    name: Optional[str] = None


@dataclass
class VectorStoreRequest:
    chunks: int

@dataclass
class VectorStoreResponse:
    code: int
    response: str


@dataclass
class VectorRetrievalResponse:
    code: int
    response: bytes


@dataclass
class QueryRequest:
    query: str


@dataclass
class QueryResponse:
    code: int
    detail: str
