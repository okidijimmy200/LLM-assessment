from config.loader import Configuration

config = Configuration()


class Config:
    openai_api_key: str
    db_faiss_path: str

    def setup(self) -> None:
        self.db_faiss_path = config.get("DB_FAISS_PATH")
