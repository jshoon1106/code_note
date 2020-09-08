import os
import imageio
from read_folder import FilesInFolder

filePath = input("write a folder direction... ")
extention = input("write a file extention you want to find... ")
videos = FilesInFolder(filePath, extention)
if not os.path.isdir(filePath+"\\gifs"):
    os.makedirs(filePath+"\\gifs")

for i, video in enumerate(videos):
    print("<<file "+str(i+1)+" saving...>>")
    images = imageio.get_reader(filePath+"\\"+video)
    name = filePath+"\\gifs\\"+video[:-(len(extention)+1)]+".gif"
    if not os.path.isdir(name):
        imageio.mimsave(name, images)
    print("<<...done>>")


# 작동 과정
# ------------
# (비디오가 저장된 폴더)
# ---input----
# ------------
# ---output---
# (gif가 저장된 폴더)
# ------------

# 필요한 것
# 비디오 폴더의 (경로)
# (gif 파일)들을 저장할 (새로운 폴더)

# 알아야 하는 핵심 기능
# imageio.get_reader() =============== 비디오 -> 이미지 배열
# imageio.mimsave(name, images) ====== 저장할 파일이름, 이미지 배열 -> gif

# 비디오 -> 이미지 배열 -> gif