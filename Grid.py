'''
Created on Jan 11, 2014

@author: Zero
@version: 0.0.2
'''

import pygame, sys, time, random, Enemy, Shot, Base, Audio, Functions, Items
rr = random.randrange
    


def main():
    from constants import *

    #Init
    Functions.Game_Init()

    #screen
    pygame.display.set_caption("Grid Ver: {v}".format(v = version))
    screen.blit(image,(0,0))
    pygame.display.update()
    pygame.time.wait(1000)

    #First Enemies
    for i in range(enemyNum):
        ene = Enemy.RedRect(screen, enemy_speed)
        enemys.append(ene)

    '''
    Music Variables
    '''
    try:
        music = Audio.Music("normal")
    except:
        "No se pudo inicializar la musica."


    while correr:
        screen.fill((0,0,0))
        mousePos = pygame.mouse.get_pos()
        clock.tick(60)
        fps = clock.get_fps()

        '''
        EVENT LOOP
        '''
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    if wlaser == True:
                        shots.append(Shot.WLaser(mousePos,shots))
                    else:
                        shots.append(Shot.Laser(mousePos,shots))
            if e.type == pygame.KEYDOWN and e.key == pygame.K_1:
                if wlaser == True:
                    wlaser = False
                else:
                    wlaser = True
            if e.type == pygame.KEYDOWN and e.key == pygame.K_m:
                for shots in shot:
                    shot.bullet_speed -= 5
            if e.type == pygame.KEYDOWN and e.key == pygame.K_n:
                for shot in shots:
                    shot.bullet_speed += 5
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                pause = True
                music.pause()
                while pause:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()
                        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                            pause = False
                            break
                music.unpause()

        '''
        GAME LOGICS
        '''

        for i in enemys:
            i.update()

        for i in shots:
            i.update(screen)

        for i in explosion:
            i.update(screen)

        try:
            if not music.music_stop():
                Functions.Winner(True,screen,base.hp)
        except:
            pass

        for i in items:
            i.update(screen)
            if i.rect.bottom > base.rect.top:
                base.hp += 10
                i.kill(items)

        #Enemies loop | Damage Manager

        """
        for i in enemys:
            for s in shots:
                if i.rect.colliderect(s.rect):
                     i.hp -= 5
                if i.hp == 0:
                    drop = i.drop()
                    explosion.append(Enemy.Explosion(explosion,i.rect.centerx,i.rect.centery,1,1))
                    explosion.append(Enemy.Explosion(explosion,i.rect.centerx,i.rect.centery,1,-1))
                    explosion.append(Enemy.Explosion(explosion,i.rect.centerx,i.rect.centery,-1,1))
                    explosion.append(Enemy.Explosion(explosion,i.rect.centerx,i.rect.centery,-1,-1))
                i.kill(enemys)
                if drop:
                    if len(items) < 3:
                        items.append(i.item())
            if i.rect.y >= base.rect.y:
                enemys.remove(i)
                base.hp -= i.damage
        """

        for i in enemys:
            if pygame.sprite.spritecollide(i, shots, False):
                i.hp -= 5
                if i.hp == 0:
                    drop = i.drop()
                    explosion.append(Enemy.Explosion(explosion,i.rect.centerx,i.rect.centery,1,1))
                    explosion.append(Enemy.Explosion(explosion,i.rect.centerx,i.rect.centery,1,-1))
                    explosion.append(Enemy.Explosion(explosion,i.rect.centerx,i.rect.centery,-1,1))
                    explosion.append(Enemy.Explosion(explosion,i.rect.centerx,i.rect.centery,-1,-1))
                i.kill(enemys)
                if drop:
                    if len(items) < 3:
                        items.append(i.item())
            if i.rect.y >= base.rect.y:
                enemys.remove(i)
                base.hp -= i.damage

        if len(enemys) == 0:
            enemyNum = 45
            if enemy_speed < 5:
                enemy_speed += 1
            for enemy in range(enemyNum):
                ene = Enemy.RedRect(screen,enemy_speed)
                enemys.append(ene)
                if enemy >= 40:
                    ene = Enemy.BlueRect(screen,enemy_speed-1)
                    enemys.append(ene)

        if base.hp <= 0:
            gameover = True
            try:
                music.stop()
            except Exception, e:
                print e
            break
            


        '''
        SCREEN DRAW
        '''
        base.update(screen)
        Functions.DisplayDataInfo(fps)
        pygame.display.update()

    Functions.GameOver(gameover,screen)

if __name__ == "__main__":
    main()
