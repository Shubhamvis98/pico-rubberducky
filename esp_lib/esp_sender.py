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
        sleep_ms(len(str(line))*40)
        self.LED.value(1)

    def send_serial(self):
        if self.ducky == None:
            print("[!]Input file is None.\n")
            return
        print('Injecting...')
        with open(self.ducky, 'r') as file:
            for i in file.readlines():
                self.send_line(i)
        
    def shell(self):
        while True:
            inp = input('# ')
            try:
                if inp.split()[0].isupper():
                    self.send_line(f'\n{inp}')
                else:
                    self.send_line(f'STRING {inp}\nENTER')
            except:
                self.send_line(f'\nENTER')


if __name__ == '__main__':
    duck = DUCKY('ducky.txt')
    duck.send_serial()
