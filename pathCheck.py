import os

def check(fileName, Path):
    filePath = os.path.join(Path, fileName)
    if os.path.exists(filePath):
        print('Yeah the file exists at the path')
    else:
        print('Nope the file doesn\'t exist at the path')
