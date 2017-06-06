import RPi.GPIO as GPIO

import time

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)

GPIO.setup(18, GPIO.OUT)

GPIO.setup(27, GPIO.OUT)

from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/index')
@app.route('/')
def index():

 return render_template('index.html')

@app.route('/redledon')

def redledon():

 GPIO.output(17, GPIO.HIGH)

 #return "Red LED on"
 return redirect(url_for('index'))

@app.route('/redledoff')

def redledoff():

 GPIO.output(17, GPIO.LOW)

 return "Red LED off"

@app.route('/greenledon')

def greenledon():

 GPIO.output(18, GPIO.HIGH)

 return "Green LED on"

@app.route('/greenledoff')

def greenledoff():

 GPIO.output(18, GPIO.LOW)

 return "Green LED off"

@app.route('/blueledon')

def blueledon():

 GPIO.output(19, GPIO.HIGH)

 return "Blue LED on"

@app.route('/blueledoff')

def blueledoff():

 GPIO.output(19, GPIO.LOW)

 return "Blue LED off"

if __name__ == "__main__":

 app.run(host='0.0.0.0')
