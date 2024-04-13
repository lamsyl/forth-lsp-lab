import sys

from jsonrpc import JSONRPCResponseManager
from jsonrpc.dispatcher import Dispatcher

def add(a, b):
    return a + b

def full_name(**kwargs):
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    return f"{first_name} {last_name}"

def run_stdio():
    dispatcher = Dispatcher({
        "add": add,
        "full_name": full_name,
    })

    for line in sys.stdin:
        response = JSONRPCResponseManager.handle(
            line, dispatcher)
        print(response.json)

if __name__ == '__main__':
    print("==== Local call ====")
    print(add(2, 3))
    print(full_name(first_name="Haskell", last_name="Curry"))

    print("==== Remote call via stdio: read request from stdin, output response to stdout ====")
    run_stdio()
