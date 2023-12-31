from flask import request, Response
from flask import Blueprint, jsonify
from models.models import DocRequest, QueryRequest
import server.server, logfile

document_api = Blueprint("document_api", __name__)


@document_api.route("/api/vi/document/upload-csv", methods=["POST"])
def upload_csv():
    try:
        csv_file: dict = request.files
        response = server.server.clean_store_service.clean_store_csv(
            DocRequest(csv_file.get("csv"))
        )

        if response.code != 200:
            return Response(status=response.code, response=response.detail)

        return jsonify(
            {"code": response.code, "reason": response.detail, "name": response.name}
        )
    except Exception as e:
        logfile.get_logger().error(f"-Error " + f"{type(e).__name__} {str(e)}")
        return Response(status=500, response="Internal Server Error")


@document_api.route("/api/vi/document/query-document", methods=["POST"])
def query_document():
    try:
        data: dict = request.get_json()
        response = server.server.document_qa_service.question_answer(QueryRequest(data.get("query")))

        if response.code != 200:
            return Response(status=response.code, response=response.detail)

        return jsonify({"code": response.code, "reason": response.detail})
    except Exception as e:
        logfile.get_logger().error(f"-Error " + f"{type(e).__name__} {str(e)}")
        return Response(status=500, response="Internal Server Error")
