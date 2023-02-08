# AUTHOR: SHUBHAM VISHWAKARMA
# GITHUB: SHUBHAMVIS98

import network
from time import sleep
from machine import Pin


LED = Pin(2, Pin.OUT)

def blink(times):
    for i in range(times):
        sleep(0.1)
        LED.value(0)
        sleep(0.1)
        LED.value(1)

def wlan(ssid, passwd):
    sta = network.WLAN(network.STA_IF)
    ap = network.WLAN(network.AP_IF)
    ap.active(False)
    sta.active(True)
    sta.connect(ssid, passwd)
    sleep(5)
    if sta.isconnected():
        blink(5)
        return sta.ifconfig()[0]
    else:
        sta.active(False)
        ap.active(True)
        ap.config(essid='MicPy', password='MicropythoN')
        blink(2)
        return ap.ifconfig()[0]

