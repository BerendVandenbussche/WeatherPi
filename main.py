from temperature import temperature
from flask import Flask, jsonify, request, url_for, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
endpoint = '/api/v1'
temperature = temperature(27, '28-00000aee38a9')

@app.route(endpoint + '/pool/temperature', methods=['GET'])
def get_pool_temperature():
    if (request.method == 'GET'):
        return jsonify(temperature.read_one_wire_temperature())

@app.route(endpoint + '/weather/temperature', methods=['GET'])
def get_temperature():
    if (request.method == 'GET'):
        return jsonify(temperature.read_temperature_humidity_sensor().get('temperature'))

@app.route(endpoint + '/weather/humidity', methods=['GET'])
def get_humidity():
    if (request.method == 'GET'):
        return jsonify(temperature.read_temperature_humidity_sensor().get('humidity'))


if __name__ == '__main__':
    Flask.run(app, host="0.0.0.0", port=5500)
