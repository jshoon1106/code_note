import os
path = input("input file path.... ")
ext = input("input video extention you want to find... ")
for filename in os.listdir(path):
    if filename.endswitch(ext):
        os.system('ffmpeg -y -i {0} -vf "transpose=1"'.format(filename))