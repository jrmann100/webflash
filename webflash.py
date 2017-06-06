import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

isOn = False

@app.route('/index')
@app.route('/')
def index():

 return render_template('index.html')

@app.route('/redledon')

def redledon():

 GPIO.output(17, GPIO.HIGH)

 return "Red LED on"
 #return redirect(url_for('index'))

@app.route('/redledoff')

def redledoff():

 GPIO.output(17, GPIO.LOW)

 return "Red LED off"
 #return redirect(url_for('index'))

if __name__ == "__main__":

 app.run(host='0.0.0.0')
