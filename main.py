from motor_control.motor_control import Motor
from time import sleep

if __name__ == "__main__":
    left = Motor(pin=4, debug=True)
    left.initialize_motor()
    left.set_power(0.5)
    sleep(4)
    left.set_power(-0.5)
    sleep(4)
    left.stop()