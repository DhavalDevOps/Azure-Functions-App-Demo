import azure.functions as func
import json

bp = func.Blueprint()

@bp.function_name(name="PreviewUsers")
@bp.route(route="preview/users", methods=["GET"])
def preview_users(req: func.HttpRequest) -> func.HttpResponse:
    users = [
        {"id": 1, "name": "Alice"},
        {"id": 2, "name": "Bob"}
    ]

    return func.HttpResponse(
        json.dumps(users),
        mimetype="application/json"
    )
