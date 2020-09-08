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
    fps = images.get_meta_data()['fps']
    name = filePath+"\\gifs\\"+video[:-(len(extention)+1)]+".gif"
    if not os.path.isdir(name):
        with imageio.get_writer(name) as writer:
            for i, img in enumerate(images):
                if i%2 == 0:
                    writer.append_data(img)
                    print("img "+str(i+1)+"appending... ")

# gif파일의 용량을 줄이려면
# 앞뒤로 변화하는 프레임만 추가하는 것이다!
        


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
# .get_meta_data()['fps'] ============ 비디오가 몇 프레임인지 알아냄