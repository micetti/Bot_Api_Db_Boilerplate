# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify

from api_request_solver import save_station_data, create_or_join_flat

app = Flask(__name__)

@app.route("/station_data/", methods=['POST'])
def station_data():
    save_station_data(request.json)
    return "OK"

@app.route("/put/", methods=['POST'])
def put_money():
    pass

@app.route("/list/", methods=['POST'])
def get_list():
    pass

@app.route("/name/", methods=['POST'])
def set_name():
    pass

@app.route("/flat/", methods=['POST'])
def flat():
    create_or_join_flat(request.json)
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)