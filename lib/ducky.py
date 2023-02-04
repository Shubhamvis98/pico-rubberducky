# AUTHOR: SHUBHAM VISHWAKARMA
# GITHUB/TWITTER: SHUBHAMVIS98

from time import sleep
import board
import busio
import digitalio
import usb_hid
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

class DUCKY:
    DEFAULT_DELAY = 200
    LED = digitalio.DigitalInOut(board.GP25)
    uart = busio.UART(board.GP0, board.GP1, baudrate=115200)
    CAPS = None

    KEYS = {
        'A':Keycode.A, 'B':Keycode.B, 'C':Keycode.C, 'D':Keycode.D, 'E':Keycode.E, 'F':Keycode.F, 'G':Keycode.G,
        'H':Keycode.H, 'I':Keycode.I, 'J':Keycode.J, 'K':Keycode.K, 'L':Keycode.L, 'M':Keycode.M, 'N':Keycode.N,
        'O':Keycode.O, 'P':Keycode.P, 'Q':Keycode.Q, 'R':Keycode.R, 'S':Keycode.S, 'T':Keycode.T, 'U':Keycode.U,
        'V':Keycode.V, 'W':Keycode.W, 'X':Keycode.X, 'Y':Keycode.Y, 'Z':Keycode.Z,
        'ONE':Keycode.ONE, 'TWO':Keycode.TWO, 'THREE':Keycode.THREE, 'FOUR':Keycode.FOUR, 'FIVE':Keycode.FIVE,
        'SIX':Keycode.SIX, 'SEVEN':Keycode.SEVEN, 'EIGHT':Keycode.EIGHT, 'NINE':Keycode.NINE, 'ZERO':Keycode.ZERO,
        '1': Keycode.ONE, '2': Keycode.TWO, '3': Keycode.THREE, '4': Keycode.FOUR, '5': Keycode.FIVE,
        '6': Keycode.SIX, '7': Keycode.SEVEN, '8': Keycode.EIGHT, '9': Keycode.NINE, '0': Keycode.ZERO,
        'ENTER':Keycode.ENTER, 'RETURN':Keycode.RETURN,
        'ESCAPE':Keycode.ESCAPE, 'BACKSPACE':Keycode.BACKSPACE, 'TAB':Keycode.TAB, 'SPACEBAR':Keycode.SPACEBAR,
        'SPACE':Keycode.SPACE, 'MINUS':Keycode.MINUS, 'EQUALS':Keycode.EQUALS, 'LEFT_BRACKET':Keycode.LEFT_BRACKET,
        'RIGHT_BRACKET':Keycode.RIGHT_BRACKET, 'BACKSLASH':Keycode.BACKSLASH, 'POUND':Keycode.POUND,
        'SEMICOLON':Keycode.SEMICOLON, 'QUOTE':Keycode.QUOTE, 'GRAVE_ACCENT':Keycode.GRAVE_ACCENT, 'COMMA':Keycode.COMMA,
        'PERIOD':Keycode.PERIOD, 'FORWARD_SLASH':Keycode.FORWARD_SLASH, 'CAPS_LOCK':Keycode.CAPS_LOCK, 'F1':Keycode.F1,
        'F2':Keycode.F2, 'F3':Keycode.F3, 'F4':Keycode.F4, 'F5':Keycode.F5, 'F6':Keycode.F6, 'F7':Keycode.F7, 'F8':Keycode.F8,
        'F9':Keycode.F9, 'F10':Keycode.F10, 'F11':Keycode.F11, 'F12':Keycode.F12, 'PRINT_SCREEN':Keycode.PRINT_SCREEN,
        'SCROLL_LOCK':Keycode.SCROLL_LOCK, 'PAUSE':Keycode.PAUSE, 'INSERT':Keycode.INSERT, 'HOME':Keycode.HOME,
        'PAGE_UP':Keycode.PAGE_UP, 'DELETE':Keycode.DELETE, 'END':Keycode.END, 'PAGE_DOWN':Keycode.PAGE_DOWN,
        'RIGHT_ARROW':Keycode.RIGHT_ARROW, 'LEFT_ARROW':Keycode.LEFT_ARROW, 'DOWN_ARROW':Keycode.DOWN_ARROW,
        'UP_ARROW':Keycode.UP_ARROW, 'KEYPAD_NUMLOCK':Keycode.KEYPAD_NUMLOCK,
        'KEYPAD_FORWARD_SLASH':Keycode.KEYPAD_FORWARD_SLASH, 'KEYPAD_ASTERISK':Keycode.KEYPAD_ASTERISK,
        'KEYPAD_MINUS':Keycode.KEYPAD_MINUS, 'KEYPAD_PLUS':Keycode.KEYPAD_PLUS, 'KEYPAD_ENTER':Keycode.KEYPAD_ENTER,
        'KEYPAD_ONE':Keycode.KEYPAD_ONE, 'KEYPAD_TWO':Keycode.KEYPAD_TWO, 'KEYPAD_THREE':Keycode.KEYPAD_THREE,
        'KEYPAD_FOUR':Keycode.KEYPAD_FOUR, 'KEYPAD_FIVE':Keycode.KEYPAD_FIVE, 'KEYPAD_SIX':Keycode.KEYPAD_SIX,
        'KEYPAD_SEVEN':Keycode.KEYPAD_SEVEN, 'KEYPAD_EIGHT':Keycode.KEYPAD_EIGHT, 'KEYPAD_NINE':Keycode.KEYPAD_NINE,
        'KEYPAD_ZERO':Keycode.KEYPAD_ZERO, 'KEYPAD_PERIOD':Keycode.KEYPAD_PERIOD, 'KEYPAD_BACKSLASH':Keycode.KEYPAD_BACKSLASH,
        'APPLICATION':Keycode.APPLICATION, 'POWER':Keycode.POWER, 'KEYPAD_EQUALS':Keycode.KEYPAD_EQUALS, 'F13':Keycode.F13,
        'F14':Keycode.F14, 'F15':Keycode.F15, 'F16':Keycode.F16, 'F17':Keycode.F17, 'F18':Keycode.F18, 'F19':Keycode.F19,
        'F20':Keycode.F20, 'F21':Keycode.F21, 'F22':Keycode.F22, 'F23':Keycode.F23, 'F24':Keycode.F24,
        'LEFT_CONTROL':Keycode.LEFT_CONTROL, 'CTRL':Keycode.CONTROL, 'CONTROL':Keycode.CONTROL, 'LEFT_SHIFT':Keycode.LEFT_SHIFT,
        'SHIFT':Keycode.SHIFT, 'LEFT_ALT':Keycode.LEFT_ALT, 'ALT':Keycode.ALT, 'OPTION':Keycode.OPTION, 'LEFT_GUI':Keycode.LEFT_GUI,
        'GUI':Keycode.GUI, 'WINDOWS':Keycode.WINDOWS, 'COMMAND':Keycode.COMMAND, 'RIGHT_CONTROL':Keycode.RIGHT_CONTROL,
        'RIGHT_SHIFT':Keycode.RIGHT_SHIFT, 'RIGHT_ALT':Keycode.RIGHT_ALT, 'RIGHT_GUI':Keycode.RIGHT_GUI
        }

    def __init__(self, ducky):
        self.ducky = ducky
#         self.LED = digitalio.DigitalInOut(board.GP25)
        self.LED.direction = digitalio.Direction.OUTPUT
        self.LED.value = True
        self.kbd = Keyboard(usb_hid.devices)
        self.layout = KeyboardLayout(self.kbd)
        self.send = self.kbd.send
        self.press = self.kbd.press
        self.release = self.kbd.release
#         self.uart = busio.UART(board.GP0, board.GP1, baudrate=115200)

    def caps_rst(self, toggle=0, CAPS=0):
        if not toggle:
            self.kbd.press(Keycode.CAPS_LOCK)
            sleep(.1)
            self.kbd.release(Keycode.CAPS_LOCK)
            if self.kbd.led_on(Keyboard.LED_CAPS_LOCK):
                self.kbd.send(Keycode.CAPS_LOCK)
            CAPS = 0
        elif(toggle == 1 and CAPS == 0):
            self.kbd.send(Keycode.CAPS_LOCK)
            CAPS = 1

    def modkey(self, keys):
        for i in range(len(keys)):
            keys[i] = keys[i].upper()
        if len(keys) == 1:
            self.send(self.KEYS[keys[0]])
        elif len(keys) == 2:
            self.send(self.KEYS[keys[0]], self.KEYS[keys[1]])
        elif len(keys) == 3:
            self.send(self.KEYS[keys[0]], self.KEYS[keys[1]], self.KEYS[keys[2]])

    def f_word(self, word, line):
        if(word == 'REM' or word == '#'):
          return 'COMMENT'  

        elif(word == 'STRING'):
            self.layout.write(line.strip()[7:])
        
        elif(word == 'DELAY'):
            sleep(DEFAULT_DELAY/1000) if len(line) == 5 else sleep(int(line[6:])/1000)

        elif(word in self.KEYS):
            self.modkey(line.split())
        
        else:
            return ('NOT FOUND: '+ word)
        
    def run(self):
        print(f'Executing {self.ducky}...')
        with open(self.ducky, 'r') as ducky:
            duck = ducky.readlines()

        for line in range(len(duck)):
            if duck[line]:
                self.f_word(duck[line].split()[0], duck[line])
        self.LED.value = False
        sleep(1)

if __name__ == '__main__':
    duck = DUCKY('ducky.txt')
    duck.run()

