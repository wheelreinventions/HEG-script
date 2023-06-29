import shutil
from os import listdir
from os.path import isfile, isdir, join

image_dir = 'D:/Develop/HEGtools/5000003320310/'
dirs = [f for f in listdir(image_dir) if isdir(join(image_dir, f))]
for dir in dirs :
    source = join(image_dir, dir)
    files = [f for f in listdir(source)]
    file = join(source, files[0])
    shutil.copy2(file, image_dir)
