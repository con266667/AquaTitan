import sys
from time import sleep
import math

class Motor:

    def __init__(self, pin, debug=False, min_pwr = 0.06, neutral_pwr = 0.075, max_pwr = 0.09):
        self.pin = pin
        self.debug = debug
        self.min_pwr = min_pwr
        self.neutral_pwr = neutral_pwr
        self.max_pwr = max_pwr
        self.cur_pwr = 0

    def echo_to_file(self, st: str):
        original_stdout = sys.stdout
        with open('/dev/pi-blaster', 'w') as f:
            sys.stdout = f  # Change the standard output to the file we created.
            print(st)
            sys.stdout = original_stdout  # Reset the standard output to its original value
            
    def set_pwr(self, pwr):
        if self.debug:
            print("Setting power to:", pwr)
        self.cur_pwr = pwr
        self.echo_to_file("{}={}".format(str(self.pin), str(pwr)))
        
    def max_power(self):
        self.set_pwr(self.max_pwr)
        
    def min_power(self):
        self.set_pwr(self.min_pwr)
        
    def neutral_power(self):
        self.set_pwr(self.max_pwr)
        
    def glide_to(self, pwr):
        mult = -1 if pwr < self.cur_pwr else 1
        while not math.isclose(self.cur_pwr, pwr, abs_tol=0.001):
            self.set_pwr(self.cur_pwr + mult * 0.0001)
            sleep(0.003)
        self.set_pwr(pwr)
    
    def set_power(self, power):
        '''From -1 to 1'''
        pwr = (power + 1) / 2
        pwr = (self.max_pwr - self.min_pwr) * pwr + self.min_pwr
        
        if (self.cur_pwr > self.neutral_pwr and pwr < self.neutral_pwr):
            self.glide_to(self.neutral_pwr)
            sleep(1)
            self.set_pwr(pwr)
            sleep(1)
            self.glide_to(self.neutral_pwr)
            sleep(1)
        self.glide_to(pwr)
        
    def initialize_motor(self):
        self.set_pwr(self.neutral_pwr)
        sleep(5)
        
    def stop(self):
        self.set_pwr(self.neutral_pwr)
        sleep(1)
        self.set_pwr(0)
        