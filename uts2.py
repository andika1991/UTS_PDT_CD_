import cv2
from google.colab import files

uploaded = files.upload()  
image_name = list(uploaded.keys())[0]
image = cv2.imread(image_name)
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
