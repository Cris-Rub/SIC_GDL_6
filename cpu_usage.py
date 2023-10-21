from gpiozero import LED
import psutil
from time import sleep
from datetime import datetime
led_yellow = LED(20)
led_red = LED(21)
file=open("log.txt","w")

while True:
    cpu_usage = psutil.cpu_percent(interval = 1, percpu = True)
    cpu_usage_nean = sum(i/len(cpu_usage) for i in cpu_usage)
    cpu_usage_nean = round(cpu_usage_nean,3)
    print(f"cpu usage (%) : {cpu_usage_nean}%")
    if 60 > cpu_usage_nean > 30:
        led_yellow.on()
        led_red.off()
    elif cpu_usage_nean >= 60:
        led_yellow.on()
        led_red.on()
    else:
        led_yellow.off()
        led_red.off()
    data =  f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}" \
            f"cpu usage (%) : {cpu_usage_nean}%\n"
    file.write(data)
    sleep(1)
    file.close()