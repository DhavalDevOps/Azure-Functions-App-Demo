import azure.functions as func
import json
import logging

bp = func.Blueprint()

@bp.function_name(name="IngestAlerts")   # 👈 Azure Portal name
@bp.route(route="alerts/ingest", methods=["POST"])
def ingest_alerts(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("IngestAlerts triggered")

    try:
        data = req.get_json()

        return func.HttpResponse(
            json.dumps({
                "message": "Alerts ingested successfully",
                "count": len(data) if isinstance(data, list) else 1
            }),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as e:
        logging.error(str(e))
        return func.HttpResponse(
            json.dumps({"error": str(e)}),
            status_code=500,
            mimetype="application/json"
        )
