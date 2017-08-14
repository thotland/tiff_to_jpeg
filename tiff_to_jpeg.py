# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from PIL import Image
import os


def findPic():
    rootlist = []
    for root, _, files in os.walk('C:\Users\jeromy\Pictures\New folder'):
        for thisfile in files:
            if thisfile.endswith('.tiff'):
                rootlist.append(os.path.join(root, thisfile))
    return rootlist, root

def formatPic(rootlist, root):
    for pic in rootlist:
        src = pic
        newPicParts = pic.split('.')
        newPic = newPicParts[-2]
        dst = newPic +'.jpeg'
        img = Image.open(src)
        img.save(dst)
        
if __name__ == "__main__":
    print('Looking for your TIFFs...')
    rootlist, root = findPic()
    formatPic(rootlist, root)
    print('Program finished')