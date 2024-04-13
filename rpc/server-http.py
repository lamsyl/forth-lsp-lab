from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager
from jsonrpc.dispatcher import Dispatcher

def add(a, b):
    return a + b

def full_name(**kwargs):
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    return f"{first_name} {last_name}"

@Request.application
def application(request):
    dispatcher = Dispatcher({
        "add": add,
        "full_name": full_name,
    })
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')

if __name__ == '__main__':
    print("==== Local call ====")    
    print(add(2, 3))
    print(full_name(first_name="Haskell", last_name="Curry"))

    print("==== Remote call via HTTP: POST http://localhost:4000/jsonrpc ====")
    run_simple('localhost', 4000, application)
