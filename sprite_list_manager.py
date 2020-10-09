'''Sprite list module'''

import os
import turtle

class SpriteListManager():
    """Prepares the list of sprite GIFs"""
    def __init__(self):
        '''Manage the lists of sprites module'''
        load_images_to_list("Resources\\ShaunAnimation\\Shaun_Right")

def load_images_to_list(folder_name):
    """Prepares a list of sprite GIFs from a folder"""
    if os.path.exists(folder_name):
        filelist = os.listdir(folder_name) #Note UNIX folder=file
        for filename in filelist:
            turtle.register_shape(folder_name + "\\" + filename)
    else:
        raise Exception("Error loading images from " + folder_name + " - Check path?")
