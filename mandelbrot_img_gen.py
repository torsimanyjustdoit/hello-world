# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 20:40:02 2015

@author: polbaladas
"""
from PIL import Image

def isMandelBrot(c):
    z = complex(0)
    flag = False
    for i in range(100):
        z = complex(z*z+c)    
        if z.real*z.real + z.imag*z.imag >=4:
            flag=True            
            break

    if flag :
        return False
    else:
        return True

def drawImage(n, m, r):
    img = Image.new( 'RGB', (m,m), "white")
    
    x = -2
    y = -1.5
    
    for i in range(img.size[0]):
        y = -1.5
        for j in range(img.size[1]):
            c = complex(x/r,y/r)
            if isMandelBrot(c):
                img.putpixel((i,j),(0,0,0))
            y+=n
        x+=n
    img.show()
    
drawImage(0.01, 300,1)