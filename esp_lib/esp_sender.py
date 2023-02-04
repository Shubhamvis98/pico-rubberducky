# AUTHOR: SHUBHAM VISHWAKARMA
# GITHUB: SHUBHAMVIS98

from machine import Pin, UART
from time import sleep_ms


class DUCKY:
    def __init__(self, ducky=None):
        self.ducky = ducky
        self.LED = Pin(2, Pin.OUT)
        self.LED.value(1)
        self.uart = UART(0, 115200)

    def send_line(self, line):
        self.LED.value(0)
        self.uart.write(str(line) + '\n')
        sleep_ms(len(str(line))*15)
        self.LED.value(1)

    def send_serial(self):
        if self.ducky == None:
            print("[!]Input file is None.\n")
            return
        print('Injecting...')
        with open(self.ducky, 'r') as file:
            for i in file.readlines():
                self.send_line(i)
        

if __name__ == '__main__':
    duck = DUCKY('ducky.txt')
    duck.send_serial()
