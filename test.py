from motor_control.motor_control import Motor
from camera_control.camera_control import Camera
from time import sleep
import numpy as np

def test_motor():
    left = Motor(pin=4, debug=True)
    left.initialize_motor()
    left.set_power(0.5)
    sleep(4)
    left.set_power(-0.5)
    sleep(4)
    left.set_power(-0.3)
    sleep(4)
    left.set_power(0.3)
    sleep(4)
    left.set_power(-0.7)
    sleep(4)
    left.stop()
    
def test_camera():
    camera = Camera(0, 0)
    camera.initialize_camera()
    camera.save_image("test.png")
    camera.stop()

if __name__ == "__main__":
    test_motor()
    test_camera()
