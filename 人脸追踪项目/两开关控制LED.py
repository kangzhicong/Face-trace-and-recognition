import RPi.GPIO as gpio
from time import sleep
from random import randint

R,G,B = 11,13,15
k1,k2 = 12,16

winner = 0
gpio.setmode(gpio.BOARD)

gpio.setup(R,gpio.OUT)
gpio.setup(G,gpio.OUT)
gpio.setup(B,gpio.OUT)
gpio.setup(k1,gpio.IN)
gpio.setup(k2,gpio.IN)

gpio.output(R,gpio.HIGH)
gpio.output(G,gpio.HIGH)
gpio.output(B,gpio.HIGH)

sleep(3)

gpio.output(R,gpio.LOW)
gpio.output(G,gpio.LOW)
gpio.output(B,gpio.LOW)

while True:
    if gpio.input(k1) == gpio.HIGH:
        gpio.output(R,gpio.LOW)
        gpio.output(G,gpio.LOW)
        gpio.output(B,gpio.HIGH)
        break
    elif gpio.input(k2) == gpio.HIGH:
           gpio.output(R,gpio.HIGH)
           gpio.output(G,gpio.LOW)
           gpio.output(B,gpio.LOW)
           break
sleep(5)
gpio.cleanup( )


