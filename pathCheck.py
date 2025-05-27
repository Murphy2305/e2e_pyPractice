import os

def check(fileName, Path):
    dirList = os.listdir(Path)
    if fileName in dirList :
        print('file exist on the path')
    else:
        print('file does not exist on the path')


