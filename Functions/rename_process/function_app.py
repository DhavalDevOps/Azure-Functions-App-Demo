import azure.functions as func

app = func.FunctionApp()

@app.function_name(name="UserProcessor")
@app.route(route="UserProcessor", methods=["POST"])
def user_handler(req: func.HttpRequest):
    return func.HttpResponse("OK")
