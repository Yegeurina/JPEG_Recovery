import os
import types
import shutil

file_list=[]
jpegFileSig = b'\xFF\xD8\xFF\xE0'

def detectFile() :

    path_dir = input('Input File Link : ')
    file_list = os.listdir(path_dir)

    for idx,file in enumerate(file_list):
        filePath = os.path.join(path_dir,file)
        with open(filePath,mode="rb") as f:
            sig = f.read(4)
            if sig==jpegFileSig :
                recoveryFile = os.path.join(filePath+'.jpeg')
                shutil.copy2(filePath,recoveryFile)  


if __name__=='__main__' :
    detectFile()
