from pijuice import PiJuice

class solar_charging:
    def __init__(self):
        self.pijuice = PiJuice(1, 0x14)

    def get_status(self):
        return self.pijuice.status.GetStatus()

    def get_battery_percentage(self):
        return self.pijuice.status.GetChargeLevel()