'''
Other Screen stuff

-Game Over Screen
-Winner Screen
'''

import pygame, Grid, sys, constants

def Game_Init():
    try:
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
    except Exception, e:
        print e

def Grade(score):
	if score == 100:
		grade = "A+"
		return grade
	elif score >= 90:
		grade = "A"
		return grade
	elif score >= 80:
		grade = "B"
		return grade
	elif score >= 70:
		grade = "C"
		return grade
	elif score >= 60:
		grade = "D"
		return grade
	else:
		grade = "F"
		return grade

def Message(grade):
	if grade == 'A+':
		word = "Perfect"
	elif grade == 'A':
		word = "Very Good"
	elif grade == 'B':
		word = "Good"
	elif grade == 'C':
		word = "Nice"
	elif grade == 'D':
		word = "Ok"
	elif grade == "F":
		word = "You can do it better next time."

	message = "{g}  {w}".format(g=grade,w=word)
	return message

def GameOver(boolean,screen):
    font = pygame.font.SysFont("Times New Roman", 32)
    text =font.render("GameOver",True, (255,0,0))
    text2 = font.render("Presiona SPACE para jugar otra vez.",True,(255,0,0))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery
    text2Rect = text2.get_rect()
    text2Rect.centerx = screen.get_rect().centerx
    text2Rect.centery = screen.get_rect().centery + 33
    while boolean:
            screen.fill((0,0,0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    return
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    boolean = False
                    Restart()
                    Grid.main()
                    return
            screen.blit(text,textRect)
            screen.blit(text2,text2Rect)
            pygame.display.update()


def Winner(boolean,screen,score):
    font = pygame.font.SysFont("Times New Roman", 32)
    text = font.render("Winner",True, (0,235,25))
    textRect = text.get_rect()
    textRect.centerx = screen.get_rect().centerx
    textRect.centery = screen.get_rect().centery
    grade = Functions.Grade(score)
    msg = Functions.Message(grade)
    text2 = font.render(msg,True,(0,235,25))
    text2Rect = text2.get_rect()
    text2Rect.centerx = screen.get_rect().centerx
    text2Rect.centery = screen.get_rect().centery + 33
    while boolean:
            screen.fill((0,0,0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    return
                if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                    boolean = False
                    Grid.main()
                    return
            screen.blit(text,textRect)
            screen.blit(text2,text2Rect)
            pygame.display.update()

def DisplayDataInfo(fps):
    font = pygame.font.SysFont("Calibri",16)
    from constants import screen, enemys, shots, base
    enemiesText = font.render("Enemies: " + str(len(enemys)),True, (255,255,255))
    shotsText = font.render("Shots in Screen: " + str(len(shots)),True, (255,255,255))
    fpsText = font.render("FPS: " + str(int(fps)),True, (255,255,255))
    baseText = font.render("Base HP: " + str(base.hp), True, (255,255,255))
    screen.blit(enemiesText,(0,0))
    screen.blit(shotsText,(0,17))
    screen.blit(fpsText,(0,33))
    screen.blit(baseText,(0,51))

def Restart():
    #Restablecer todas las variables a su estado original.
    constants.base.hp = 100
    constants.enemys = []
    constants.shots = []
    constants.explosion = []
    constants.items = []
    
