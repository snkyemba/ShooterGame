import pygame, sys
from pygame.locals import *
from Shooter import *
from Block import *
import random
pygame.init()
screen = pygame.display.set_mode((800,600))
clock = pygame.time.Clock()
pygame.key.set_repeat(100,100)

font = pygame.font.Font('freesansbold.ttf', 20)
font2 = pygame.font.Font('freesansbold.ttf', 40)

white = (255,255,255)

p1 = Shooter(20,20)
redblocks = []
blackblocks = []
score = 0
wins = 0
losses = 0
time = 200
timecount = 0
stop = False
lose = False
end = True

# "Black blocks" are now cupcakes
# "Red blocks" are now strawberries
pygame.display.set_caption(
    'Use the arrow keys and the space bar. Get 50 points before the timer reaches 0 to win!') 
while end:
    screen.fill((255,192,203))
    p1.draw(screen)

    # Timer
    timecount += 1
    timetext = font.render('Timer: {}'.format(time), True, (0,0,0))
    timetextrect = timetext.get_rect(topleft=(650,35))
    screen.blit(timetext,timetextrect)
    if timecount%50==0 and stop == False:
        time -= 1
        if time==0:
            stop = True
            lose = True
        
    # Player score
    scoretext = font.render('Score: {}'.format(score), True, (0,0,0))
    scoretextrect = scoretext.get_rect(topleft=(650,10))
    screen.blit(scoretext,scoretextrect)
    '''
    # Total wins
    winstext = font.render('Total wins: {}'.format(wins), True, (0,0,0))
    winstextrect = winstext.get_rect(topleft=(650,35))
    screen.blit(winstext,winstextrect)

    # Total Losses
    losstext = font.render('Total losses: {}'.format(losses), True, (0,0,0))
    losstextrect = losstext.get_rect(topleft=(650,60))
    screen.blit(losstext,losstextrect)
    '''
    # Creating random black blocks    
    if random.randrange(0,100)<1 and stop == False:
        x = random.randrange(600,750)
        y = random.randrange(70,550)
        blackblocks.append(Block(x,y,50,50,
                                 pygame.image.load('cupcake.jpg')))

    # Black block movement & collision with player
    if len(blackblocks)>0:
        for item in blackblocks:
            blackrect = pygame.Rect((item.x,item.y),(50,50))
            p1rect = pygame.Rect((p1.x,p1.y),(60,50))
            collide = pygame.Rect.colliderect(blackrect,p1rect)
            if collide:
                stop = True
                lose = True  
            if stop == False:
                item.change_x(-1)
            #if item.x<0:
                #blackblocks.remove(item)
            item.draw_block(screen)
            
    # Red block movement
    if len(redblocks)>0:
        for item in redblocks:
            if stop == False:
                item.change_x(1)
            item.draw_block(screen)
            if item.x>800:
                redblocks.remove(item)
                
    # Black and red block collision
    for black in blackblocks:
        for red in redblocks:
            blackrect = pygame.Rect((black.x,black.y),(50,50))
            redrect = pygame.Rect((red.x,red.y),(15,18))
            collide = pygame.Rect.colliderect(blackrect,redrect)
            if collide:
                if black in blackblocks:
                    blackblocks.remove(black)
                redblocks.remove(red)
                score += 5
                
    # Player wins            
    if score >= 50:
        stop = True
        wintext = font2.render('YOU WIN', True, (255,53,203))
        wintextrect = wintext.get_rect(center=(400,300))
        screen.blit(wintext,wintextrect)
        #wins += 1
        
    # Player loses
    if lose == True:
        losetext = font2.render('GAME OVER', True, (255,53,203))
        losetextrect = losetext.get_rect(center=(400,300))
        screen.blit(losetext,losetextrect)
        #losses += 1
        
    # Play again
    if stop == True:
        againtext = font2.render('Play again?', True, white,(255,53,203))
        againtextrect = againtext.get_rect(center=(400,450))
        screen.blit(againtext,againtextrect)
    
    pygame.display.update()
    clock.tick(300)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type==KEYDOWN and event.key==K_ESCAPE):
            end = False
            pygame.quit()
        if event.type == KEYDOWN and stop == False:
            if ((event.key == K_DOWN or event.key == K_s) and (
                p1.y<600-p1.height)):
                p1.change_y(10)
            if ((event.key == K_UP or event.key == K_w) and (
                p1.y>0)):
                p1.change_y(-10)
            if (event.key == K_SPACE):
                redblocks.append(Block(90,p1.y,15,18,
                                       pygame.image.load('strawberry.jpg')))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if stop == True:
                if againtextrect.collidepoint(pygame.mouse.get_pos()):
                    p1.x = 20
                    p1.y = 20
                    score = 0
                    time = 200
                    blackblocks.clear()
                    redblocks.clear()
                    lose = False
                    stop = False
                    
                

                
