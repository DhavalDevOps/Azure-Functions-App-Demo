import json
import logging
import azure.functions as func



# app = func.FunctionApp()

# @app.function_name(name="UserProcessor")
# @app.route(route="user/process", methods=["POST"])

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    Azure Function entry point.
    The function name is defined in function.json (not here).
    """

    logging.info("UserProcessor function triggered")

    try:
        # Read JSON body
        try:
            body = req.get_json()
        except ValueError:
            body = {}

        user_id = body.get("user_id")
        action = body.get("action", "none")

        if not user_id:
            return func.HttpResponse(
                json.dumps({
                    "error": "user_id is required"
                }),
                status_code=400,
                mimetype="application/json"
            )

        # Example business logic
        result = {
            "message": "User processed successfully",
            "user_id": user_id,
            "action": action
        }

        return func.HttpResponse(
            json.dumps(result),
            status_code=200,
            mimetype="application/json"
        )

    except Exception as exc:
        logging.exception("Unhandled exception")

        return func.HttpResponse(
            json.dumps({
                "error": "Internal Server Error",
                "details": str(exc)
            }),
            status_code=500,
            mimetype="application/json"
        )
