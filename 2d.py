from pico2d import *

import os
import math

os.getcwd()
os.chdir("C:\\Users\\myeos\\OneDrive\\문서\\GitHub\\파이썬\\2DGP-Drill2")

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x=0
y=90

while(1):
    clear_canvas_now()
    
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        x=x+2
        character.draw_now(x,y)
        delay(0.01)

    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        x=x-1
        y=y+1
        character.draw_now(x,y)
        delay(0.01)
        
    while(y>60):
        clear_canvas_now()
        grass.draw_now(400,30)
        y=y-1
        character.draw_now(x,y)
        delay(0.01)

    
    while(y<300):
        a=1
        clear_canvas_now()
        grass.draw_now(400,30)
        x=x+a
        y=y+1
        character.draw_now(x,y)
        delay(0.01)
        a+=1

    while(y<600):
        a=1
        clear_canvas_now()
        grass.draw_now(400,30)
        x=x-a
        y=y+1
        character.draw_now(x,y)
        delay(0.01)
        a+=1
        
    while(y>300):
        a=1
        clear_canvas_now()
        grass.draw_now(400,30)
        x=x-a
        y=y-1
        character.draw_now(x,y)
        delay(0.01)
        a+=1

    while(y>0):
        a=1
        clear_canvas_now()
        grass.draw_now(400,30)
        x=x+a
        y=y-1
        character.draw_now(x,y)
        delay(0.01)
        a+=1

        
   



close_canvas()
