import cv2
import numpy as np

c = cv2.imread("img.jpg")
c = cv2.resize(c, (10240, 10240), cv2.INTER_LANCZOS4)
cv2.imwrite("out.jpg", c)