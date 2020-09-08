import os
def FilesInFolder(path, extention, short=True):
    return [file if short else path+"\\"+file for file in os.listdir(path) if file.endswith(extention)]