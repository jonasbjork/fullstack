#!/usr/bin/env python3
import os
from flask import Flask, request, jsonify


def summa(a, b):
    return a + b


def differens(a, b):
    return a - b


app = Flask(__name__)


@app.route('/')
def hello():
    name = os.getenv('NAMN', 'World')
    return f"Hello {name}! Use <a href='/summa?a=10&b=5'>/summa?a=10&b=5</a>" \
        " or <a href='/differens?a=10&b=5'>/differens?a=10&b=5</a> " \
        "to calculate."


def get_numbers():
    a = int(request.args['a'])
    b = int(request.args['b'])
    return a, b


@app.route('/summa')
def add():
    result = get_numbers()
    if isinstance(result, tuple):
        a, b = result
        return jsonify(result=summa(a, b))
    return result


@app.route('/differens')
def subtract():
    result = get_numbers()
    if isinstance(result, tuple):
        a, b = result
        return jsonify(result=differens(a, b))
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
