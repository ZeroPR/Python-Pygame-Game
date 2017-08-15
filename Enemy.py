'''
Created on Jan 15, 2014

@author: Zero
'''

import pygame, random, Items
rr = random.randrange
ru = random.uniform

class EnemyRect(pygame.sprite.Sprite):
    _doc = """La clase maestra para todos los enemigos en forma de cuadrados.

    Atributos:
        damage -> el da~o que efectuara a la base si la toca.
        hp -> vida de el objeto

    Metodos:
        update() -> dibuje el sprite en la pantalla o superficie agregada al parametro de contructor.
        kill(lista) -> elimina el objeto de la lista o grupo donde se encuentra.
        drop() -> crea un numero random y return True si es mayor a la condicion.
                  Este metodo va de la mano con el metodo item().
        item() -> return un item.
    """
    image = ''
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = ''
        self.rect = ''
        self.screen = ''

    def __doc__(self):
        print self._doc

    def update(self):
        if self.rect.bottom >= 0:
            self.screen.blit(self.image,self.rect)
        self.rect.move_ip(0,self.speed)

    def kill(self, lista):
        if self.hp <= 0:
            lista.remove(self)

    def set(self, screen):
        self.rect.x = rr(screen.get_width()-50)
        self.rect.y = -rr(100,3000)

    def drop(self):
        pass

    def item(self):
        pass

class RedRect(EnemyRect):
    '''
    Rectangulos enemigos.
    '''
    damage = 5

    def __init__(self,screen,speed):
        EnemyRect.__init__(self)
        self.width, self.height = 50,50
        self.image = pygame.Surface((self.width,self.height))
        pygame.draw.rect(self.image,(220,0,0),[0,0,50,50],1)
        self.rect = self.image.get_rect()
        self.set(screen)
        self.hp = 5
        self.speed = speed
        self.screen = screen


    def drop(self):
        ranNum = ru(0,100)
        if ranNum < 10.0:
            return True

    def item(self):
        return Items.Vida([self.rect.centerx,self.rect.centery])

class BlueRect(EnemyRect):
    '''
    Rectangulos Azules, tienes mas resitensias que los rojos.
    '''
    damage = 10

    def __init__(self,screen,speed):
        EnemyRect.__init__(self)
        self.width, self.height = 50,50
        self.image = pygame.Surface((self.width,self.height))
        pygame.draw.rect(self.image,(0,0,220),[0,0,50,50],1)
        self.rect = self.image.get_rect()
        self.set(screen)
        self.hp = 50
        self.speed = speed
        self.screen = screen


    def drop(self):
        return False

    def item(self):
        return Items.Vida([self.rect.centerx,self.rect.centery])



class Explosion():
    '''
    Efecto de explosion cuando un enemy es eliminado.
    '''
    def __init__(self,lista,x,y,movex,movey):
        self.image = pygame.Surface((10,10))
        self.red = 200
        self.green = 100
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image,(self.red,self.green,0),[0,0,10,10])
        self.rect.centerx = x
        self.rect.centery = y
        self.duration = 25
        self.movex = movex
        self.movey = movey
        self.lista = lista
    def update(self,surface):
        pygame.draw.rect(self.image,(self.red,self.green,0),[0,0,10,10])
        surface.blit(self.image,self.rect)
        self.rect.move_ip(self.movex,self.movey)
        self.duration -= 1
        if self.green > 0:
            self.green -= 5
        if self.duration <= 0:
            self.kill(self.lista)

    def kill(self,lista):
        lista.remove(self)
