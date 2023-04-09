import cv2
import time
from multiprocessing import Process, Value, Pipe
import numpy as np

class Camera:
    def __init__(self, matrix_coefficients, distortion_coefficients, aruco_dict_type = cv2.aruco.DICT_6X6_50, image_dir = "/home/connor/Desktop/AquaTitan/images/"):
        self.matrix_coefficients = matrix_coefficients
        self.distortion_coefficients = distortion_coefficients
        self.aruco_dict_type = aruco_dict_type
        self.image_dir = image_dir
        
    def camera_process(self, camera_on, conn):
        self.cap = cv2.VideoCapture(0)

        while camera_on.value:
            ret, frame = self.cap.read()
            if not ret:
                break
            conn.send(frame)
            time.sleep(0.01)

        self.cap.release()
        
    def initialize_camera(self):
        self.camera_on = Value('i', 1)
        self.parent_conn, child_conn = Pipe()
        self.p = Process(target=self.camera_process, args=(self.camera_on, child_conn))
        self.p.start()
        while np.all(self.get_frame() == 0):
            pass
        print("Camera initialized")
        
    def stop(self):
        self.camera_on.value = 0
        self.p.terminate()
        
    def get_frame(self):
        return self.parent_conn.recv()
    
    def save_image(self, filename):
        cv2.imwrite(self.image_dir + filename, self.get_frame())
        print("Image saved")
        
    def get_position(self):
        frame = self.get_frame()
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.aruco_dict = cv2.aruco.Dictionary_get(self.aruco_dict_type)
        parameters = cv2.aruco.DetectorParameters_create()


        corners, ids, _ = cv2.aruco.detectMarkers(gray, cv2.aruco_dict,parameters=parameters,
            cameraMatrix=self.matrix_coefficients,
            distCoeff=self.distortion_coefficients)

        if len(corners) > 0:
            res = []
            for i in range(0, len(ids)):
                rvec, tvec, _ = cv2.aruco.estimatePoseSingleMarkers(
                    corners[i], 0.02, self.matrix_coefficients, self.distortion_coefficients)
                res.append((ids[i], rvec, tvec))
            return res