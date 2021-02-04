import pygame
import sys
from pygame.locals import *
pygame.init()

width = 1200
height = 700

clock = pygame.time.Clock()
ground = pygame.display.set_mode((width,height))

smallfont = pygame.font.SysFont("comicsansms",  25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)

# Game naming
pygame.display.set_caption("Soccer")

black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (56,123,255)

#adding players, background and ball
character_1 = pygame.image.load("P1.png").convert()
character_2 = pygame.image.load("P2.png").convert()
ball = pygame.image.load("football.jpeg").convert()
background = pygame.image.load("football field.jpg").convert()

ground.blit(ball, (0,0))
ground.blit(character_1, (0,300))
ground.blit(character_2, (0,600))
ground.blit(background, (0,0))

pygame.display.flip()

ballArea = ball.get_rect()
character_1_Area = character_1.get_rect()
character_2_Area = character_2.get_rect()

#Starting point of the ball
ballArea.left= 600
ballArea.top= 350

#Starting point of player 1
character_1_Area.left = 160
character_1_Area.top = 280

#Starting point of player 2
character_2_Area.left = 1033
character_2_Area.top = 280

speed = [1,1]

# Adding scoreboard
def score(player_1, player_2):
    scoreboard = smallfont.render("{player_1} : Player 1 vs Player 2 : {player_2} ", True, black)
    ground.blit(scoreboard, [0,0])

while True:
    
    for action in pygame.event.get():
        if action.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if action.type == KEYDOWN:
            if action.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    ballArea.move_ip(speed)
# ball exit constraint
    if ballArea.left < 0 or ballArea.right > width:
        speed[0] = -speed[0]
    if ballArea.top < 0 or ballArea.bottom > height:
        speed[1] = -speed[1]
        
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
            
# player 2 movement
    keystroke = pygame.key.get_pressed()
    if keystroke[K_LEFT]:
        character_2_Area.move_ip((-1,0))
    if keystroke[K_RIGHT]:
        character_2_Area.move_ip((1,0))
    if keystroke[K_DOWN]:
        character_2_Area.move_ip((0,1))
    if keystroke[K_UP]:
        character_2_Area.move_ip((0,-1))
        
#player 1 movement
    keystroke = pygame.key.get_pressed()
    if keystroke[K_a]:
        character_1_Area.move_ip((-1,0))
    if keystroke[K_d]:
        character_1_Area.move_ip((1,0))
    if keystroke[K_s]:
        character_1_Area.move_ip((0,1))
    if keystroke[K_w]:
        character_1_Area.move_ip((0,-1))

#updating background, players and other images
    ground.fill(black)
    ground.blit(background,(0,0))
    ground.blit(ball, ballArea)
    ground.blit(character_1, character_1_Area)
    ground.blit(character_2, character_2_Area)

    pygame.display.flip()
    #clock.tick(600)
