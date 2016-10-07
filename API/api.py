# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify

from api_request_solver import answer_hello_world, increase_counter_and_inform, save_message, get_five_last_answers

app = Flask(__name__)

@app.route("/")
def hello():
    return answer_hello_world()

@app.route("/count/")
def count():
    return increase_counter_and_inform()

@app.route("/echo/", methods=['POST'])
def echo():
    response_messages = get_five_last_answers()
    save_message(content=request.json)
    return response_messages


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)