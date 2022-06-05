import RPi.GPIO as GPIO

class rain:
    def __init__(self, rain_pin=None, rain_bucket_content_mm=0):
        self.rain_pin = rain_pin
        self.rain_bucket_content_mm = rain_bucket_content_mm
        self.bucket_tips = 0
        self.rain_amount = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(rain_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.add_event_detect(self.rain_pin, GPIO.FALLING, callback=self.bucket_tipped)

    
    def _calculate_rain_amount(self):
        self.rain_amount = self.bucket_tips * self.rain_bucket_content_mm


    def bucket_tipped(self, bucket_pin):
        self.bucket_tips += 1
        self._calculate_rain_amount()

    
    def reset_rain(self):
        self.bucket_tips = 0
        self.rain_amount = 0
        