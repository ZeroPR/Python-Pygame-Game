#Aqui estare bregando con los niveles del juego.
import pygame

class Level():
	default = None

	def __init__(self, w, h, background_image = None, player):
		self.width, self.height = w, h
		if background_image:
			self.bg = background_image
		else:
			self.bg = default_bg
		self.enemies = []
		self.player = player

	def update(self,screen):
		screen.blit(self.background_image,(0,0))
		

	def get_player_pos(self):
		return player.pos()
