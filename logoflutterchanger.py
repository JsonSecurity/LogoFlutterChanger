#!/usr/bin/env python3

from PIL import Image
from time import sleep as delay

import uscript as u
import cv2
import shutil
import os
import glob
import sys
import signal

def signal_handler(sig, frame):
    print(f'\n\n{u._A} Saliendo...')
    sys.exit(1)

signal.signal(signal.SIGINT, signal_handler)

def ShowImages(path):
    files = glob.glob(f'{path}\\**\\*.png', recursive=True)
    u.bar(1, "Verifying", 80)

    if not files:
        print(f'\n{u._T} No image found\n')
        sys.exit(1)

    print(f'\n{u._T} Path images\n')
    for file in files:
        print(f'{u._V} {file[17:]}')
        delay(.1)
    
    return files

def VerifyPath(message="Path Android Project"):
    while True:
        path = input(f'\n{u._Q} {message}: ')
        if not os.path.exists(path):
            u.clear()
            print(u.banner)
            print(f"\n{u._A} The path does not exist")
            continue
        #if "AndroidStudio" not in path:
        #    u.clear()
        #    print(u.banner)
        #    print(f"\n{u._A} Enter the path of *AndroidStudio*")
        #    continue
        break
    
    #u.clear()
    #print(u.banner)
    return path

def ShowSizes(files):
    print(f'\n{u._T} Showing sizes\n')
    sizes = []
    for ruta_imagen in files:
        with Image.open(ruta_imagen) as img:
            original_size = img.size
            print(f"{u._V} Image:{u._B} {ruta_imagen[-15:]}{u._E} Size:{u._B} {original_size}")
            sizes.append(original_size)
            delay(.1)
    return sizes

def VerifyImage(image_path):
    try:
        with Image.open(image_path) as img:
            if img.format not in ["PNG", "JPEG"]:
                print(f"\n{u._A} is not a PNG or JPG image")
    except IOError:
        print(f"\n{u._A} is not a valid image file")
        sys.exit(1)

def ResizeImage(image_path, files, sizes):
    print(f'\n{u._T} Resize image\n')

    for i in range(len(files)):
        # image replace
        shutil.copy2(image_path, files[i])
        #image resize
        with Image.open(files[i]) as img_resize:
            image_resized = img_resize.resize(sizes[i])
            image_resized.save(files[i])
            print(f"{u._V} Saved:{u._B} {files[i][-15:]}{u._E} Size:{u._B} {sizes[i]}")
        
        delay(.1)

def LogoChanger():
    print(f'\n{u._T} Logo Flutter Changer')

    path = VerifyPath()

    files = ShowImages(path)
    sizes = ShowSizes(files)

    image_path = VerifyPath("Image path")
    
    VerifyImage(image_path)
    ResizeImage(image_path, files, sizes)

if __name__ == '__main__':
    u.clear()
    print(u.banner)

    LogoChanger()
