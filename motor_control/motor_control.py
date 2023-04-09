import sys

class MotorController:

    def __init__(pin, min_pwr = 0.06, neutral_pwr = 0.075, max_pwr = 0.09):
        self.pin = pin
        self.min_pwr = min_pwr
        self.neutral_pwr = neutral_pwr
        self.max_pwr = max_pwr

    def echo_to_file(st: str):
        original_stdout = sys.stdout
        with open('/dev/pi-blaster', 'w') as f:
            sys.stdout = f  # Change the standard output to the file we created.
            print(st)
            sys.stdout = original_stdout  # Reset the standard output to its original value
            
    def set_pwr(self, pwr):
        echo_to_file(str(self.pin) + "=" + str(pwr))
        
    def initialize_motor():
        set_pwr(neutral_pwr)
        sleep(2)
        