import RPi.GPIO as GPIO
import math
from apscheduler.schedulers.background import BackgroundScheduler

class wind:
    def __init__(self, anemometer_pin=None, anemometer_radius_cm = 9.0):
        scheduler = BackgroundScheduler()
        self.anemometer_pin = anemometer_pin
        self.anemometer_radius_cm = anemometer_radius_cm
        self.spin_amount = 0
        self.loop_interval = 5
        self.wind_speed = None
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(anemometer_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.anemometer_pin, GPIO.FALLING, callback=self.register_spin)
        scheduler.add_job(self._calculate_wind_speed, 'interval', seconds=self.loop_interval)
        scheduler.start()

    def _calculate_wind_speed(self):
        circumference_cm = (2 * math.pi) * self.anemometer_radius_cm
        rotations = self.spin_amount / 2.0
        distance_km = (circumference_cm * rotations) / 100000.0

        km_per_sec = distance_km / self.loop_interval
        km_per_hour = km_per_sec * 3600

        self.wind_speed = km_per_hour
        self.reset_anemometer_spins()


    def register_spin(self, pin):
        self.spin_amount += 1

    
    def reset_anemometer_spins(self):
        self.spin_amount = 0
        