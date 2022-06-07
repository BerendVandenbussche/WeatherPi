import RPi.GPIO as GPIO
from apscheduler.schedulers.background import BackgroundScheduler

class rain:
    def __init__(self, rain_pin=None, rain_bucket_content_mm=0):
        scheduler = BackgroundScheduler()
        self.rain_pin = rain_pin
        self.rain_bucket_content_mm = rain_bucket_content_mm
        self.bucket_tips = 0
        self.mm_per_hour = 0
        self.loop_interval = 5
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(rain_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.rain_pin, GPIO.FALLING, callback=self.bucket_tipped)
        scheduler.add_job(self._calculate_mm_per_hour, 'interval', minutes=self.loop_interval)
        scheduler.start()

    
    def _calculate_mm_per_hour(self):
        self.mm_per_hour = self.bucket_tips * self.rain_bucket_content_mm * (60/self.loop_interval)
        self.reset_rain()


    def bucket_tipped(self, bucket_pin):
        self.bucket_tips += 1

    
    def reset_rain(self):
        self.bucket_tips = 0
        