import azure.functions as func
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    response = {
        "status": "UP",
        "service": "azure-functions-demo",
        "version": "1.0.0"
    }

    return func.HttpResponse(
        json.dumps(response),
        status_code=200,
        mimetype="application/json"
    )
