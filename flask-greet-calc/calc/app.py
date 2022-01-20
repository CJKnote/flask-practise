from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_nums():
    """takes in query params a and b and adds them together"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    res = add(a,b)

    return str(res)

@app.route('/sub')
def sub_nums():
    """gives the results a-b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    res = sub(a,b)

    return str(res)

@app.route('/mult')
def mult_nums():
    """gives the results a*b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    res = mult(a,b)

    return str(res)

@app.route('/div')
def div_nums():
    """gives the results dividing a by b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    res = div(a,b)

    return str(res)


operations = {
    "add": add,
    "sub": sub,
    "mult": mult,
    "div": div
}
#making a route that can deal with 4 different functions
@app.route('/math/<operation>')
def math_nums(operation):
    """will preform the operation from the URL param with the query params a and b"""
    a = int(request.args["a"])
    b = int(request.args["b"])

    res = operations[operation](a,b)

    return str(res)