'''Modulos para probar los sprites y scripts'''
import pygame, Items, sys, random
pygame.init()

rr = random.randrange


screen = pygame.display.set_mode((350,350))
clock = pygame.time.Clock()
running = True
items = []

#List
for i in range(0,11):
    x = x * 2
    y = y * 2
    item = Items.XP([x,y])
    items.append(item)


while running:
    screen.fill((0,0,0))
    clock.tick(30)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

	for i in items:
		i.update(screen)

	pygame.display.update()

sys.exit()