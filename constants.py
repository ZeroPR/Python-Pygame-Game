#-------------------------------------------------------------------------------
# Name:        constants
# Purpose:     variables
#
# Author:      zero
#
# Created:     01/04/2014
# Copyright:   (c) rper7268 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame, Base, Enemy, Shot,Audio, Items

version = "0.0.2"

#Screen Variables
screen_width, screen_height = 640,640
screen = pygame.display.set_mode((screen_width,screen_height))

#Settings
clock = pygame.time.Clock()
pygame.mouse.set_cursor(*pygame.cursors.diamond)
font = pygame.font.SysFont("Times New Roman", 16)

 #Logo
image = pygame.image.load("res/image/gridlogo.png").convert()
image = pygame.transform.scale(image,(screen_width,screen_height))


'''
List
'''
enemys = []
shots = []
explosion = []
items = []

'''
Base Data
'''

base = Base.Base()

'''
Enemies
'''
enemyNum = 25
enemy_speed = 3


'''
Some Variable
'''
correr = True
gameover = False
pause = False
wlaser = False


