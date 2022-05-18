class temperature:

    def read_one_wire_temperature(sensor_address):
        W1_path = '/sys/bus/w1/devices/{0}/w1_slave'.format(address)