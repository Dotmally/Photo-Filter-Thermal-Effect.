#This Code will use the implementation of the pygame module to create a window and change the rgb values of each pixel diplayed in each  photo.

import sys
import pygame as py
import random
py.init()
Theimage = input( 'please type in the image file name within the same directory as the code.' )
#transfer the image to pygame
img=py.image.load(Theimage)
#getting the size of the image
(W,H)=img.get_size()
window=py.display.set_mode((W*2,H*2))

#we need to translate the pixels into luminance then assign  each luminance a coloured square
for y in range(H):
    for x in range(W):
        (r, g, b,_) = img.get_at((x, y))
        #check the black areas
        lumi = (0.2126 * r + 0.7152 * g + 0.0788 * b) * 255
        red=int(r/50)
        green=int(g/50)
        blue=int(b/50)
        while red>0:
            if lumi >0.625:
                py.draw.circle(window,(255,0,0),(random.randint((x*5)-18,(x*5)),random.randint((y*5)-18,(y*5))),1)
                red-=1
        while green>0:
            if lumi>0.625:
                py.draw.circle(window,(0,255,0),(random.randint((x*5)-18,(x*5)),random.randint((y*5)-18,(y*5))),1)
                green-=1
        while blue>0:
            if lumi>0.625:
                py.draw.circle(window,(0,0,255),(random.randint((x*5)-18,(x*5)),random.randint((y*5)-18,(y*5))),1)
                blue-=1
py.display.update()
while True:
    for event in py.event.get():
        if event.type == py.QUIT:
            exit()