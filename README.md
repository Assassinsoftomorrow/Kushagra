# Head Soccer
  # Two player soccer game using pygame.
  
  import pygame
import sys
from pygame.locals import *
import time

pygame.init()

p1won = 0
p2won = 0

#Naming the game.
pygame.display.set_caption("Head Soccer")

width = 1200
height =700

ground = pygame.display.set_mode((width, height))

#Font sizes.
smallfont = pygame.font.SysFont("comicsansms",  25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

#Colours
black = (0,0,0)
red = (255,0,0)
green =(0,255,0)
blue = (56, 123, 255)

#Round won messages.
p1_scores = medfont.render("Player 1 scores !", True, red)
p2_scores = medfont.render("Player 2 scores !", True, red)

#Importing images for players, football, field
character_1 = pygame.image.load("P1.png").convert()
character_2 = pygame.image.load("P2.png").convert()
ball = pygame.image.load("football.jpeg").convert()
background = pygame.image.load("football field.jpg").convert()
post1 = pygame.image.load("post.jpg").convert()
post2 = pygame.image.load("post2.jpg").convert()

ground.blit(ball, [0,0])
ground.blit(background, [0,0])
ground.blit(character_1, [0,0])
ground.blit(character_2, [0,0])
ground.blit(post1, [0,0])
ground.blit(post2, [0,0])

pygame.display.flip()

ballArea = ball.get_rect()
character_1_Area = character_1.get_rect()
character_2_Area = character_2.get_rect()
post_1_Area = post1.get_rect()
post_2_Area = post2.get_rect()

#Defining the starting point of the ball
ballArea.left= 600
ballArea.top= 350

#Starting point of player 1
character_1_Area.left = 160
character_1_Area.top = 280

#Starting point of player 2
character_2_Area.left = 1033
character_2_Area.top = 280

#Location of post 1
post_1_Area.left = 35
post_1_Area.top = 257

#Location of post 2
post_2_Area.left = 1100
post_2_Area.top = 257

speed = [1,1]

#Creating scoreboard
board1 = smallfont.render("Player 1 : " + str(p1won), True, black, blue)
board2 = smallfont.render("Player 2 : " + str(p2won), True, black, blue)

def player_1_move():
    keystroke = pygame.key.get_pressed()

    if keystroke[K_a]:
        character_1_Area.move_ip((-1,0))
    if keystroke[K_d]:
        character_1_Area.move_ip((1,0))
    if keystroke[K_s]:
        character_1_Area.move_ip((0,1))
    if keystroke[K_w]:
        character_1_Area.move_ip((0,-1))

def player_2_move():
    keystroke = pygame.key.get_pressed()

    if keystroke[K_LEFT]:
        character_2_Area.move_ip((-1,0))
    if keystroke[K_RIGHT]:
        character_2_Area.move_ip((1,0))
    if keystroke[K_DOWN]:
        character_2_Area.move_ip((0,1))
    if keystroke[K_UP]:
        character_2_Area.move_ip((0,-1))

def ball_exit():
    if ballArea.left < 0 or ballArea.right > width:
        speed[0] = -speed[0]
    if ballArea.top < 0 or ballArea.bottom > height:
        speed[1] = -speed[1]

def ball_collision():
 #player 1 and ball collision
    if character_1_Area.colliderect (ballArea):
        if character_1_Area.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
        if character_1_Area.colliderect(ballArea.move(0,speed[1])):
            speed[0] = -speed[0]

# player 2 and ball collision
    if character_2_Area.colliderect (ballArea):
        if character_2_Area.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
        if character_2_Area.colliderect(ballArea.move(0,speed[1])):
            speed[0] = -speed[0]

def goal():
    #Scoring a goal for player 2
    if post_1_Area.colliderect(ballArea):
        if post_1_Area.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
            
    if post_1_Area.colliderect(ballArea):
        if post_1_Area.colliderect(ballArea.move(0, speed[1])):
            speed[0] = -speed[0]

    #Scoring a goal for player 1
    if post_2_Area.colliderect(ballArea):
        if post_2_Area.colliderect(ballArea.move(-speed[0],0)):
            speed[1] = -speed[1]
    if post_2_Area.colliderect(ballArea):
        if post_2_Area.colliderect(ballArea.move(0, speed[1])):
            speed[0] = -speed[0]

def player_exit():
#Player 1 screen exit prevention.
    if character_1_Area.left > width:
        character_1_Area.right = 0

    if character_1_Area.right < 0:
        character_1_Area.left = width

    if character_1_Area.top > height:
        character_1_Area.bottom = 0

    if character_1_Area.bottom < 0:
        character_1_Area.top = height

#Player 2 screen exit prevention.
    if character_2_Area.left > width:
        character_2_Area.right = 0

    if character_2_Area.right < 0:
        character_2_Area.left = width

    if character_2_Area.top > height:
        character_2_Area.bottom = 0

    if character_2_Area.bottom < 0:
        character_2_Area.top = height

def p2_score_count():
    if post_1_Area.colliderect(ballArea):
#        p2won += 1
        ground.blit(p2_scores, [450,190])
        pygame.display.update()
        pygame.time.wait(2000)

#        return(p2won)

def p1_score_count():
    if post_2_Area.colliderect(ballArea):
#        p1won += 1
        ground.blit(p1_scores, [450,190])
        pygame.display.update()
        pygame.time.wait(2000)

#        return(p1won)

def playgame():

    while True:

        ballArea.move_ip(speed)

        ball_exit()
        goal()
        #p1won =
        p1_score_count()
        #p2won =
        p2_score_count()
        ball_collision()
        player_1_move()
        player_2_move()
        player_exit()
   
        for action in pygame.event.get():
            if action.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if action.type == KEYDOWN:
                if action.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
           # if  p1won == 7 or p2won ==7:
            #    pygame.quit()
            #    sys.exit()

#Updating background
        ground.blit(background, [0,0])
        ground.blit(post1, post_1_Area)
        ground.blit(post2, post_2_Area)
        ground.blit(character_1, character_1_Area)
        ground.blit(character_2, character_2_Area)
        ground.blit(board1, [50,0])
        ground.blit(board2, [1000,0])
        ground.blit(ball, ballArea)

        pygame.display.flip()

playgame()
