from pijuice import PiJuice
import subprocess

class system:
    def __init__(self):
        self.pijuice = PiJuice(1, 0x14)

    def get_status(self):
        return self.pijuice.status.GetStatus().get('data')


    def get_battery_percentage(self):
        return self.pijuice.status.GetChargeLevel().get('data')


    def get_system_uptime(self):
        return subprocess.run(['uptime'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip('\n')
