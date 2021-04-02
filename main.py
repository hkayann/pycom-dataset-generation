import time
import pycom
import machine
from pycoproc_1 import Pycoproc
from machine import RTC
from network import WLAN
from SI7006A20 import SI7006A20

def connect_wifi():
    wlan = WLAN(mode=WLAN.STA)
    wlan.connect(ssid='Glide', auth=(WLAN.WPA2, '')) # Example SSID & Password, change accordingly.
    while not wlan.isconnected():
        machine.idle()
    print("WiFi connected succesfully")

def get_real_time():
    timestamp = ""
    rtc = RTC(id=0)
    time.sleep(3)
    rtc.ntp_sync("0.uk.pool.ntp.org") # Returns tuple.
    real_time = list(rtc.now())
    real_time  = real_time[:-2 or None] # Removes microseconds and tmz.
    return real_time

def concat_list(list):
    str_time = ""
    for time in list:
        str_time += str(time)
    return str_time

if __name__ == "__main__":
    py = Pycoproc(Pycoproc.PYSENSE)
    si = SI7006A20(py)
    pycom.heartbeat(False)
    pycom.rgbled(0x0A0A08) # White.
    connect_wifi()
    with open('data.txt','w') as f:
        while True:
            try:
                temp  = str(si.temperature())
                hum =  str(si.humidity())
                timestamp = concat_list(get_real_time())
                power = str(py.read_battery_voltage())
                f.write(timestamp+","+temp+","+hum+","+power+"\n")
                print(temp+hum)
                time.sleep(2)
            except KeyboardInterrupt:
                print("Done.")
                break
