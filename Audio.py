'''
Created on Feb 18, 2014

@author: Zero
'''
import pygame, random

rr = random.randrange(0,6)

pygame.init()

class Music():
    '''
    Esta clase manejara la musica del juego.
    '''
    #music = {"normal":pygame.mixer.music.load("res/audio/music/KOTOKO - Princess Bride!.mp3")}
    music = ["res/audio/music/HIGH & HIGH.mp3",
            "res/audio/music/KOTOKO - Princess Bride!.mp3",
             "res/audio/music/AURORA.mp3",
             "res/audio/music/INNOCENCE.mp3",
             "res/audio/music/Reunion.mp3",
             "res/audio/music/Beautiful ground.mp3"]

    def __init__(self,mode):
        self.mode = mode
        pygame.mixer.music.load(self.music[rr])
        pygame.mixer.music.play()
        
        
    def stop(self):
    	pygame.mixer.music.stop()

    def pause(self):
    	pygame.mixer.music.pause()

    def unpause(self):
    	pygame.mixer.music.unpause()

    def music_stop(self):
    	return pygame.mixer.music.get_busy()
  
        