#!/usr/bin/python
from flask import Flask
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(24, GPIO.OUT)
print(GPIO.input(24))
GPIO.output(24, 0)


app = Flask(__name__)


@app.route('/off_pins')
def on_pins():
    GPIO.output(24, 1)
    print(GPIO.input(24))
    return "LED deactivated"


@app.route('/on_pins')
def off_pins():
    GPIO.output(24, 0)
    print(GPIO.input(24))
    return "LED activated"

if __name__ == '__main__':
    try:
       app.run(host='0.0.0.0', port=8000, debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()

