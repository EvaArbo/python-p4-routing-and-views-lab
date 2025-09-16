#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Python Operations with Flask Routing and Views</h1>"

@app.route("/print/<string:value>")
def print_string(value):
    print(value)
    return value

@app.route("/count/<int:num>")
def count(num):
    numbers=[str(i) for i in range (num)]
    return "\n".join(numbers) + "\n"

@app.route("/math/<int:num1>/<operation>/<int:num2>")
def math(num1, operation,num2):
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result =num1-num2
    elif operation == "*":
        result = num1*num2
    elif operation == "div":
        result= num1/num2
    elif operation == "%":
        result= num1 % num2
    else:
        return f"invalid operation {operation}"
    return str(result)


if __name__ == '__main__':
    app.run(port=5555, debug=True)
