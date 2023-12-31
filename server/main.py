import logfile
from flask_cors import CORS
from server.server import get_app
from service.service import CleanStoreService, DocumentQAService
from storage.storage import VectorStore
from config.config import Config

config = Config()
config.setup()

logfile.setup_logger("my_logger")

if __name__ == "__main__":
    app = get_app(CleanStoreService(), DocumentQAService(VectorStore(config)))
    CORS(app)
    app.run(host="0.0.0.0", port=8000, debug=True)
