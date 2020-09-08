from cv2 import cv2
import os

filePath = input("write file path... ")

img = cv2.imread(filePath, -1)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 이미지를 뽑아낸다!