import RPi.GPIO as GPIO
import drivers
import adafruit_dht
import board
from gpiozero import Button
from picamera import PiCamera
from time import sleep, time
from datetime import datetime
from threading import Thread


led_yellow = 13
led_red = 26
pir = 25
ultra_trig = 21
ultra_echo = 20

lcd = drivers.Lcd()
dht = adafruit_dht.DHT11(board.D6)
camera = PiCamera()
button = Button(12)

GPIO.setmode(GPIO.BCM)
GPIO.setup(led_yellow, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(pir, GPIO.IN)
GPIO.setup(ultra_trig, GPIO.OUT)
GPIO.setup(ultra_echo, GPIO.IN)