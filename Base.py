'''
Created on Jan 16, 2014

@author: Zero
'''
import pygame


class Base(pygame.sprite.Sprite):
    """
    Esta es la base que tienes que defender.
    """

    level = 0

    def __init__(self):
        self.hp = 100
        self.image = pygame.Surface((640,30))
        self.rect = self.image.get_rect()
        self.rect.y = 610

    def update(self,surface):
        if self.hp > 80:
            pygame.draw.rect(self.image,(0,200,0),[0,0,640,30])
        elif self.hp > 60:
            pygame.draw.rect(self.image,(100,200,0),[0,0,640,30])
        elif self.hp > 40:
            pygame.draw.rect(self.image,(150,150,0),[0,0,640,30])
        elif self.hp > 20:
            pygame.draw.rect(self.image,(200,100,0),[0,0,640,30])
        elif self.hp > 0:
            pygame.draw.rect(self.image,(200,0,0),[0,0,640,30])
        surface.blit(self.image,self.rect)

    def lvlup(self):
        pass