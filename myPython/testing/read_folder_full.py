import os
# 폴더를 인풋 받는다!
path = input("write a folder direction... ")
extention = input("write file extention you want to find... ")
#   폴더에서 파일을 뽑아 낸다!
for file in os.listdir(path):
    if file.endswith(extention):
        filePath = path + "\\" + file
        print(filePath)
# 파일 목록을 아웃풋 한다!