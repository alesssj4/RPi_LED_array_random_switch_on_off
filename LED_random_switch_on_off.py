#!/usr/bin/python
import time, threading, random
import RPi.GPIO as GPIO
#import os #only if I want to clear screem and other os functions

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)

#define 'fixed' variables ;)
pin1 = 3
pin2 = 5
pin3 = 7
pin4 = 11
pin5 = 13
pin6 = 15
pin7 = 19
pin8 = 21
#count = 0

#define pin arrays
pins =[pin1, pin2, pin3, pin4, pin5, pin6, pin7, pin8]
revpins = pins[::-1]

#User input for variables
rounds = int(raw_input('Number of repeats per cycle:?'))
tw = float(raw_input('Time to wait between steps:?'))

#set initial startup values
def setuppins():
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)

def clearup():
    for pin in pins:
        GPIO.output(pin, True)

def fw(x):
    for i in range(x):
        report("Forwards", i+1)
        for pin in pins:
            GPIO.output(pin, not GPIO.input(pin))
            time.sleep(tw)

def stepf(x):
    for i in range(x):
        report("One by one FORWARD", i+1)
        for pin in pins:
            GPIO.output(pin, False)
            time.sleep(tw)
            GPIO.output(pin, True)

def stepb(x):
    for i in range(x):
        report("One by one BACK", i+1)
        for pin in revpins:
            GPIO.output(pin, False)
            time.sleep(tw)
            GPIO.output(pin, True)
        
def back(x):
    for i in range(x):
        report("Backwards", i+1)
        for pin in revpins:
            GPIO.output(pin, not GPIO.input(pin))
            time.sleep(tw)

def onoff(x):
    for i in range(x*2):
        report("On/Off", i+1)
        GPIO.output(pin1, not GPIO.input(pin1))
        GPIO.output(pin2, not GPIO.input(pin2))
        GPIO.output(pin3, not GPIO.input(pin3))
        GPIO.output(pin4, not GPIO.input(pin4))
        GPIO.output(pin5, not GPIO.input(pin5))
        GPIO.output(pin6, not GPIO.input(pin6))
        GPIO.output(pin7, not GPIO.input(pin7))
        GPIO.output(pin8, not GPIO.input(pin8))
        time.sleep(0.5)
        
def report(cycle, count):
    print cycle, "cycle, step",count

def cleargpio():
    GPIO.cleanup()
    print "GPIO Cleanup done!"  

my_list =[fw, stepf, stepb, back, onoff]

setuppins()
clearup()

try:
    while True:
        random.choice(my_list)(rounds)
except KeyboardInterrupt:
    cleargpio() 
    
   

