import Adafruit_DHT

class temperature:
    def __init__(self, temperature_humidity_sensor_pin, W1_sensor_address):
        self.temperature_humidity_sensor_pin = temperature_humidity_sensor_pin
        self.W1_sensor_address = W1_sensor_address

    def read_one_wire_temperature(self):
        W1_path = '/sys/bus/w1/devices/{0}/w1_slave'.format(self.W1_sensor_address)
        with open(W1_path, 'r') as file:
            for line in file:
                position = line.find("t=")
                if position > -1:
                    subtract = line[position:]
                    temperature_string = subtract[2:-1]
                    temperature = int(temperature_string)/1000

                    return temperature

    def read_temperature_humidity_sensor(self):
        sensor = Adafruit_DHT.DHT11
        try:
            humidity, temperature = Adafruit_DHT.read_retry(sensor, self.temperature_humidity_sensor_pin)
            return {'temperature': '{0:0.1f}C'.format(temperature), 'humidity': '{0:0.1f}%'.format(humidity) }
        except:
            raise ValueError('Failed to get reading')