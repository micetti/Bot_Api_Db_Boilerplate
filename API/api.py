# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify

from api_request_solver import save_station_data, get_five_last_answers

app = Flask(__name__)

@app.route("/station_data/", methods=['POST'])
def station_data():
    save_station_data(request.json)
    return "OK"

@app.route("/echo/")
def echo():
    return get_five_last_answers()

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)