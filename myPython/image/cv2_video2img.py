import os
from cv2 import cv2
from read_folder import FilesInFolder

filePath = input("write a folder direction... ")
extention = input("write a file extention you want to find... ")
videos = FilesInFolder(filePath, extention, short=False)

for video in videos:
    cap = cv2.VideoCapture(video)
    currentFrame = 0

    while True:
        if not os.path.isdir(video[:-(len(extention)+1)]):
            os.makedirs(video[:-(len(extention)+1)])
        ret, frame = cap.read()
        if ret:
            name = video[:-(len(extention)+1)]+"\\"+"videoFrame"+str(currentFrame)+".jpg"
            print("making..." + name)
            if not os.path.isfile(name):
                cv2.imwrite(name, frame)
                currentFrame += 1
        else: break
cap.release() 
cv2.destroyAllWindows() 

# 작동 과정
# ------------
# (비디오가 저장된 폴더)
# ---input----
# ------------
# ---output---
# (각각의 (비디오 프레임 사진)이 모인 폴더)들
# ------------

# 필요한 것
# 비디오 폴더의 (경로)
# (추출한 비디오 프레임 사진)을 저장할 (새로운 폴더)들

# 알아야 하는 핵심 기능 (cv2)
# cv2.VideoCapture(video) ============== 비디오 -> 비디오 캡쳐
# ret, frame = cap.read() ============== (반복) 비디오 한 장씩 캡처 -> frame에 저장
# cv2.imwrite(name, frame) ============= (반복) frame을 파일로 저장

# 비디오 -> 비디오 한 장씩 캡처 -> 각각을 파일로 저장