from temperature import temperature
from rain import rain
from wind import wind
from solar_charging import solar_charging
from flask import Flask, jsonify, request, url_for, json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
endpoint = '/api/v1'
temperature = temperature(27, '28-00000aee38a9')
rain = rain(21, 0.2794)
wind = wind(13)
charge = solar_charging()


@app.route(endpoint + '/pool/temperature', methods=['GET'])
def get_pool_temperature():
    if (request.method == 'GET'):
        return jsonify(temperature.read_one_wire_temperature())


@app.route(endpoint + '/pool/temperature/history', methods=['GET'])
def get_pool_temperature_history():
    if (request.method == 'GET'):
        return jsonify('Endpoint not implemented')


@app.route(endpoint + '/weather/temperature', methods=['GET'])
def get_temperature():
    if (request.method == 'GET'):
        return jsonify(temperature.read_temperature_humidity_sensor().get('temperature'))


@app.route(endpoint + '/weather/temperature/history', methods=['GET'])
def get_temperature_history():
    if (request.method == 'GET'):
        return jsonify('Endpoint not implemented')


@app.route(endpoint + '/weather/humidity', methods=['GET'])
def get_humidity():
    if (request.method == 'GET'):
        return jsonify(temperature.read_temperature_humidity_sensor().get('humidity'))


@app.route(endpoint + '/weather/humidity/history', methods=['GET'])
def get_humidity_history():
    if (request.method == 'GET'):
        return jsonify('Endpoint not implemented')


@app.route(endpoint + '/weather/rain', methods=['GET'])
def get_rain():
    if (request.method == 'GET'):
        return jsonify(rain.mm_per_hour)


@app.route(endpoint + '/weather/rain/history', methods=['GET'])
def get_rain_history():
    if (request.method == 'GET'):
        return jsonify('Endpoint not implemented')


@app.route(endpoint + '/weather/wind', methods=['GET'])
def get_wind_speed():
    if (request.method == 'GET'):
        return jsonify(wind.wind_speed)


@app.route(endpoint + '/weather/wind/history', methods=['GET'])
def get_wind_speed_history():
    if (request.method == 'GET'):
        return jsonify('Endpoint not implemented')


@app.route(endpoint + '/status', methods=['GET'])
def get_weather_station_status():
    if (request.method == 'GET'):
        return charge.get_status()


@app.route(endpoint + '/status/battery', methods=['GET'])
def get_weather_station_battery_status():
    if (request.method == 'GET'):
        return charge.get_battery_percentage()


if __name__ == '__main__':
    Flask.run(app, host="0.0.0.0", port=5500)
