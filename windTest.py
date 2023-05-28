from gpiozero import MCP3008
import time
adc = MCP3008(channel=0)
count = 0
values = []
while True:
    wind = round(adc.value*3.3,1)
    if not wind in values:
        values.append(wind)
        count+=1
        print(count)
