# AUTHOR: SHUBHAM VISHWAKARMA
# GITHUB: SHUBHAMVIS98

from time import sleep
import board
import digitalio

import usb_hid
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

# LED INIT
LED = digitalio.DigitalInOut(board.GP25)
LED.direction = digitalio.Direction.OUTPUT
LED.value = True

# BUTTON INIT
btn = digitalio.DigitalInOut(board.GP0)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.UP                # GP0+GND when Pull.UP || GP0+3V3 when Pull.DOWN

# KEYBOARD INIT
kbd = Keyboard(usb_hid.devices)
layout = KeyboardLayout(kbd)
send = kbd.send
press = kbd.press
release = kbd.release

######
DUCKY = '/ducky.txt'
DEFAULT_DELAY = 200

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

# READ DUCKY
with open(DUCKY, 'r') as file:
    txt = file.readlines()

# REMOVE SPACES
for i in range(len(txt)):
    txt[i] = txt[i].strip()

# FUNCTIONS
CAPS = None
def caps_rst(toggle=0, CAPS=0):
    if not toggle:
        kbd.press(Keycode.CAPS_LOCK)
        sleep(.1)
        kbd.release(Keycode.CAPS_LOCK)
        if kbd.led_on(Keyboard.LED_CAPS_LOCK):
            kbd.send(Keycode.CAPS_LOCK)
        CAPS = 0
    elif(toggle == 1 and CAPS == 0):
        kbd.send(Keycode.CAPS_LOCK)
        CAPS = 1

def modkey(keys):
    for i in range(len(keys)):
        keys[i] = keys[i].upper()
    if len(keys) == 1:
        send(KEYS[keys[0]])
    elif len(keys) == 2:
        send(KEYS[keys[0]], KEYS[keys[1]])
    elif len(keys) == 3:
        send(KEYS[keys[0]], KEYS[keys[1]], KEYS[keys[2]])

#     for i in keys:
#         press(KEYS[i])
#     for i in keys:
#         release(KEYS[i])

def f_word(word, line):
    if(word == 'REM' or word == '#'):
      return 'COMMENT'  

    elif(word == 'STRING'):
        layout.write(txt[line][7:])
    
    elif(word == 'DELAY'):
        sleep(DEFAULT_DELAY/1000) if len(txt[line]) == 5 else sleep(int(txt[line][6:])/1000)

    elif(word in KEYS):
        modkey(txt[line].split())
    
    else:
        return ('NOT FOUND: '+ word)

# DRIVER CODE

if btn.value:         # ONLY EXECUTE WHEN BUTTON IS NOT PRESSED (GP0+GND)
    print('INJECTING PAYLOAD\n')
    caps_rst()        # TOGGLE CAPS LOCK IF ENABLED

    for line in range(len(txt)):
        if txt[line]:
            f_word(txt[line].split()[0], line)
#             print(f'{line+1}-->', f_word(txt[line].split()[0], line) if f_word(txt[line].split()[0], line) else 'EXECUTED')
else:
    print("CODE INJECTION TERMINATED\n")

######
LED.value = False
