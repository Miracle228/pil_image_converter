from PIL import Image
import os, sys

from pathlib import Path

path = "images_to_site/"
save_dir ="images_to_site/out"

dirs = os.listdir( path )
new_folder = 'out'
if not os.path.exists(path + new_folder):
    os.makedirs(path + new_folder)
out_name = 'my_images_'

def resize():
    num = 0
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((480,355), Image.ANTIALIAS)
            imResize.save(os.path.join(save_dir, out_name + str(num)) + '.JPG', 'JPEG', quality=90)
            num+=1
resize()