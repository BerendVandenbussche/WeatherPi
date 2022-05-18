from temperature import temperature

temperature = temperature(27, '28-00000aee38a9')
print('dt11 sensor: current temperature = {temp} and humidity {hum}'.format(temp = str(temperature.read_temperature_humidity_sensor().get('temperature')), hum = str(temperature.read_temperature_humidity_sensor().get('humidity'))), 'One wire sensor: ' + str(temperature.read_one_wire_temperature()))