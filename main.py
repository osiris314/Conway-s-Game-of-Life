import pygame
import time
import random
import numpy as np
import os
import grid
import pyautogui
import pygetwindow
from PIL import Image
from connect import *
from playsound import playsound
import imageio
import pathlib



def delete_files():
    dir = 'images'
    for file in os.scandir(dir):
        os.remove(file.path)

    def createFolder(directory):
        try:
            if not os.path.exists(directory):
                os.makedirs(directory)
        except OSError:
            print ('Error: Creating directory. ' +  directory)

directory = "images"

num = 0

os.environ["SDL_VIDEO_CENTERED"]='1'

width = 1920
height = 1080

size = (width, height)

pygame.init()
pygame.display.set_caption("CONWAYS GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

black = (0, 0, 0)
blue = (0, 121, 150)
blue1 = (0,14,71)
white = (255, 255, 255)

scaler = 10
offset = 0
fps = 120

seconds = 10
frames = 120

Grid = grid.Grid(width,height, scaler, offset)

#Grid.random2d_array()
#Grid.fixed2d_array()
#Grid.fixedarray(0,0)
#Grid.full_array()
Grid.gun()

print(str(seconds*frames) + ' Images In Total !')
#createFolder('./data/')
time.sleep(1)
delete_files()
run = True
while run:
    clock.tick(fps)
    screen.fill(black)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for i in range(int(seconds*frames)):
        Grid.Conway(off_color=white, on_color=blue1, surface=screen)
        pygame.display.update()
        #time.sleep(0.1)
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'images/image_' + str(num) + '.png')
        num = num + 1
        
    break

count = 0
for path in pathlib.Path("images").iterdir():
    if path.is_file():
        count += 1

print(count)
#gif_maker()
gif_maker2(count)
