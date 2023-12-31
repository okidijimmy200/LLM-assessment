from flask import Flask
from service.interface import (
    ICleanStoreService as CleanStoreService,
    IDocumentQAService as DocumentQAService,
)
from server.routes import document_api

clean_store_service: CleanStoreService
document_qa_service: DocumentQAService


def get_app(clean_store: CleanStoreService, document_qa: DocumentQAService):
    global clean_store_service, document_qa_service

    app = Flask(__name__)

    clean_store_service = clean_store
    document_qa_service = document_qa

    app.register_blueprint(document_api, name="document")

    return app
