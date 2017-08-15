'''
Created on Jan 15, 2014

@author: Zero
'''
import pygame, random

class Laser(pygame.sprite.Sprite):
    """
    Esta clase creara una bala.
    """
    damage = 5
    bullet_speed = -5
    speed = 0

    def __init__(self,pos,lista):
        self.image = pygame.Surface((5,10)).convert_alpha()
        pygame.draw.rect(self.image,(255,255,255,25), [0,0,10,10])
        self.rect_colli = pygame.draw.rect(self.image,(255,255,255), [3,1,0,9])
        self.rect = self.image.get_rect()
        self.rect.x,self.rect.y = pos
        self.lista = lista

    def get_colli_rect(self):
        return self.rect_colli

    def update(self,screen):
        self.speed += self.bullet_speed * 0.10
        self.rect.move_ip(0,self.speed)
        screen.blit(self.image,self.rect)
        if self.rect.bottom < 0:
            self.kill()

    def kill(self):
        self.lista.remove(self)

class WLaser(pygame.sprite.Sprite):

    """
    Esta clase creara una bala ancha.
    """
    damage = 1
    bullet_speed = -2
    speed = 0

    def __init__(self,pos,lista):
        self.image = pygame.Surface((250,1)).convert_alpha()
        self.image.fill((255,255,255))
        self.rect_colli = pygame.draw.rect(self.image,(255,255,255), [3,1,0,9])
        self.rect = self.image.get_rect()
        self.rect.centerx,self.rect.centery = pos
        self.lista = lista

    def get_colli_rect(self):
        return self.rect_colli

    def update(self,screen):
        self.speed += self.bullet_speed * 0.10
        self.rect.move_ip(0,self.speed)
        screen.blit(self.image,self.rect)
        if self.rect.bottom < 0:
            self.kill()

    def kill(self):

        self.lista.remove(self)

class TMissile(pygame.sprite.Sprite):
    """
    Misil en forma de triangulo.
    """
    speed = -2
    def __init__(self,pos,lista):
        self.image = pygame.Surface(7,7).convert_alpha()
        self.rect =  pygame.draw.polygon(self.image,(255,255,255),[[4,0],[7,7],[4,3],[0,7],[4,0]],1)
        self.rect.centerx, self.rect.centery = pos
        self.lista = lista
        self.vy = 0

    def update(self):
        self.vy += speed * .10
        self.rect.move_ip(0,self.vy)
        if self.rect.bottom < 0:
            self.kill()

    def kill(self):

        self.lista.remove(self)

class Explosion(pygame.sprite.Sprite):
    """
    Parte del TMissile cuando explota.
    """

    def __init__(self,pos,lista):
        self.image = self.Surface((1,1))
        self.image.fill((255,255,255))
        self.rect = self.image.get_rect()
        
