### Generate markers
import cv2
from cv2 import aruco
import os

### --- parameter --- ###

# Save location
dir_mark = r''

# Parameter
num_mark = 4 #Number of markers
size_mark = 500 #Size of markers

### --- marker images are generated and saved --- ###
# Call marker type
dict_aruco = aruco.Dictionary_get(aruco.DICT_6X6_50)
# dict_aruco_10x10 = aruco.Dictionary_get(aruco.DICT_6X6_50)

for count in range(num_mark) :

    id_mark = count
    img_mark = aruco.drawMarker(dict_aruco, id_mark, size_mark)
    img_name_mark = '6x6_mark_id_' + str(count) + '.jpg'
    path_mark = os.path.join(dir_mark, img_name_mark)

    cv2.imwrite(path_mark, img_mark)