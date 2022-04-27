from tkinter import *
from time import sleep
import tkinter.font 
import RPi.GPIO as GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT, initial=GPIO.LOW)

led = 8
timeUnit = 0.3;

## The below morse code dictionary has been taken from https://www.geeksforgeeks.org/morse-code-translator-python/
## It has been modified to include an extra symbol (underscore) signifying the end of the code for each letter
MORSE_CODE_DICT = { 'A':'.-_', 'B':'-..._',
                    'C':'-.-._', 'D':'-.._', 'E':'._',
                    'F':'..-._', 'G':'--._', 'H':'...._',
                    'I':'.._', 'J':'.---_', 'K':'-.-_',
                    'L':'.-.._', 'M':'--_', 'N':'-._',
                    'O':'---_', 'P':'.--._', 'Q':'--.-_',
                    'R':'.-._', 'S':'..._', 'T':'-_',
                    'U':'..-_', 'V':'...-_', 'W':'.--_',
                    'X':'-..-_', 'Y':'-.--_', 'Z':'--.._',
                    '1':'.----_', '2':'..---_', '3':'...--_',
                    '4':'....-_', '5':'....._', '6':'-...._',
                    '7':'--..._', '8':'---.._', '9':'----._',
                    '0':'-----_', ', ':'--..--_', '.':'.-.-.-_',
                    '?':'..--.._', '/':'-..-._', '-':'-....-_',
                    '(':'-.--._', ')':'-.--.-_'}

def dot():
    GPIO.output(led,GPIO.HIGH)
    sleep(timeUnit)
    GPIO.output(led,GPIO.LOW)
    sleep(timeUnit)

def dash():
    GPIO.output(led,GPIO.HIGH)
    sleep(3 * timeUnit)
    GPIO.output(led,GPIO.LOW)
    sleep(timeUnit)
    
def end():
    GPIO.output(led,GPIO.LOW)
    sleep(2 * timeUnit)

def morseIterator():
    inputString = word.get()
    if(len(inputString)>12):
        inputString = inputString[:12]
    revString = inputString.upper()
    print(revString)
    for c in revString:
        mSymbol = MORSE_CODE_DICT[c]
        for c in mSymbol:
            if(c == '.'):
                dot();
            elif (c == '-'):
                dash();
            elif (c == '_'):
                end();
   
##GUI definitions
win = Tk()
win.title("LED Toggler")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

#Widget
morseCodeButton = Button(win, text = 'Run Morse Code', font = myFont, command = morseIterator, bg = 'lightblue', height = 1, width = 24)
morseCodeButton.grid(row=1, column=1)

word = Entry(win, font = myFont, width = 15)
word.grid(row=0, column = 1)

