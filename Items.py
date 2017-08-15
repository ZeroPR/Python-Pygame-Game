'''
Aqui van todos lo items del juego
	-Vida
'''

import pygame, random

rr = random.randrange

class Vida(pygame.sprite.Sprite):

    def __init__(self,pos):
	pygame.sprite.Sprite.__init__(self)
        self.speed = 0
        self.image = self.Write()
        self.rect = self.image.get_rect()
        self.rect.centerx, self.rect.centery = pos[0],pos[1]
        pygame.draw.rect(self.image,(255,255,255),[0,0,self.image.get_width(),self.image.get_height()],1)

    def Write(self):
        font = pygame.font.SysFont("Calibri",24)
        render = font.render("+",True,(255,255,255))
        return render
    
    def update(self,screen):
        self.speed += 1 * .10
        self.rect.move_ip(0,self.speed)
        screen.blit(self.image,self.rect)
    
    def kill(self,lista):
    	lista.remove(self)


class XP(pygame.sprite.Sprite):

    value = rr(2,11)

    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.value,self.value))
        self.rect = self.image.get_rect()
        self.image.fill((0,0,0))
        self.image.blit(self.Write(),self.rect.center)
        pygame.draw.rect(self.image,(255,255,0),[0,0,self.image.get_width(),self.image.get_height()],1)

    def Write(self):
        font = pygame.font.SysFont("Calibri",self.value - 1)
        render = font.render("XP",True,(255,255,0))
        return render

    def update(self,screen):
        self.rect.move_ip(0,1)
        screen.blit(self.image,self.rect)

    def kill(self,lista):
    	lista.remove(self)

