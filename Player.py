'''
Created on Feb 23, 2014

@author: Zero
'''
import pygame
class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        self.pos = pos
        self.image = pygame.Surface((5,5))
        self.rect = self.image.get_rect()
        self.rect.centerx,self.rect.centery = self.pos[0],self.pos[1]
    
    def update(self,screen):
        screen.blit(self.image,self.rect)

    def get_pos(self):
    	return (self.rect.x, self.rect.y)
        