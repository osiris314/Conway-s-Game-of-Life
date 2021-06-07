import pyautogui
import os
import imageio
import pygame
from playsound import playsound
import random
import string

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def gif_maker2(count):
    print('Done !')
    pygame.quit()
    print('Starting GIF Maker')
    folder = 'images' 
    files = [f"{folder}\\{file}" for file in os.listdir(folder)]
    images = [imageio.imread(file) for file in files]
    imageio.mimwrite('output/' + get_random_string(8) +'.gif', images, fps=count)
    print('Complete!')
    playsound('complete.mp3')