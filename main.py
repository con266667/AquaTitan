from motor_control.motor_control import Motor
from camera_control.camera_control import Camera
    
class AquaTitan:
    def __init__(self, left_motor_pin, right_motor_pin):
        self.left_motor = Motor(left_motor_pin)
        self.right_motor = Motor(right_motor_pin)
        self.camera = Camera(0, 0)
        
    def initialize_aquatitan(self):
        self.left_motor.initialize_motor()
        self.right_motor.initialize_motor()
        self.camera.initialize_camera()
        
    def find_marker(self):
        '''Rotate boat until marker is found'''
        while self.camera.get_position() == None:
            self.right_motor.set_power(1)
            self.left_motor.set_power(0)

    def navigate_to_marker(self):
        '''Navigate until the camera's position is close to the marker (or USS)'''
        pass


if __name__ == "__main__":
    aquatitan = AquaTitan(4, 17)
    aquatitan.initialize_aquatitan()
    aquatitan.find_marker()
    aquatitan.navigate_to_marker()