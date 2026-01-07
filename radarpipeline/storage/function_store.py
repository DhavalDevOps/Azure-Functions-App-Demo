import azure.functions as func
import json

bp = func.Blueprint()

@bp.function_name(name="StoreAlerts")
@bp.route(route="alerts/store", methods=["POST"])
def store_alerts(req: func.HttpRequest) -> func.HttpResponse:
    data = req.get_json()

    # Example: pretend to store in DB
    return func.HttpResponse(
        json.dumps({
            "stored": True,
            "records": len(data)
        }),
        mimetype="application/json"
    )
