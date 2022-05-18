class temperature:

    def read_one_wire_temperature(sensor_address):
        W1_path = '/sys/bus/w1/devices/{0}/w1_slave'.format(address)
        with open(W1_path, 'r') as file:
            for line in file:
                position = line.find("t=")
                if position > -1:
                    subtract = line[position:]
                    temperature_string = subtract[2:-1]
                    temperature = int(temperature_string)/1000

                    return temp

    def read_temperature_humidity_sensor():
