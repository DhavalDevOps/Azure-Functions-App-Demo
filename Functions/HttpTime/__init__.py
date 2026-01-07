import azure.functions as func
from datetime import datetime, timezone

def main(req: func.HttpRequest) -> func.HttpResponse:
    now = datetime.now(timezone.utc).isoformat()
    return func.HttpResponse(
        f"Current UTC Time: {now}",
        status_code=200
    )
