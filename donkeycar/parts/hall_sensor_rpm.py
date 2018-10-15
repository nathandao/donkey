"""
Hall sensor RPM
"""

#!/usr/bin/python3
from time import sleep
import time, math

class HallSensorRpm:
    def __init__(self, sensor, wheel_radius):
        import RPi.GPIO as GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(sensor,GPIO.IN,GPIO.PUD_UP)
        GPIO.add_event_detect(sensor, GPIO.FALLING, callback = self.calculate_elapse, bouncetime = 20)

        self.rpm = 0
        self.pulse = 0
        self.start_timer = time.time()
        self.wheel_radius = wheel_radius
        self.on = True
        self.debug = debug
        self.wheel_radius = wheel_radius

    def calculate_elapse(self, channel):
        self.pulse+=1
        self.elapse = time.time() - start_timer
        self.start_timer = time.time()

    def update(self):
        while (self.on):
            self.calculate_speed()
            #console output for debugging
            if(self.debug):
                print('seconds:', self.elapsed)
                print('distance:', self.dist_meas)
                print('velocity:', self.m_per_sec)
            sleep(0.1)

    def calculate_speed(self):
        if self.elapse !=0:
            self.rpm = 1/elapse * 60
            self.circ_cm = 2 * math.pi * self.wheel_radius
            self.dist_m = circ_cm/100
            self.m_per_sec = dist_m / elapse
            self.dist_meas = (dist_m*pulse)*1000
            return self.m_per_sec

    def run_threaded(self):
        return self.dist_meas, self.m_per_sec

    def shutdown(self):
        # indicate that the thread should be stopped
        self.on = False
        print('stopping Hall Senror RPM')
        time.sleep(.5)

        import RPi.GPIO as GPIO
        GPIO.cleanup()
