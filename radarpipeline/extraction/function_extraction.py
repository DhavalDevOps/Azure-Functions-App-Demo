import azure.functions as func
import json

bp = func.Blueprint()

@bp.function_name(name="ExtractData")
@bp.route(route="data/extract", methods=["POST"])
def extract_data(req: func.HttpRequest) -> func.HttpResponse:
    payload = req.get_json()

    return func.HttpResponse(
        json.dumps({
            "status": "extracted",
            "items": len(payload)
        }),
        mimetype="application/json"
    )
