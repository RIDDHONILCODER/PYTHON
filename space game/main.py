import math
import random
import pygame

screen_width=800
screen_height=500
player_start_x=370
PLAYER_START_Y = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
pygame.init()
screen=pygame.display.set_mode((screen_height,screen_width))
pygame.display.set_caption("space invader games ")
icon=pygame.image.load('ufo.png')
pygame.display.set_icon(icon)
bg=pygame.image.load('bg.png')
player=pygame.image.load('player.png')
playerx=player_start_x
playery=PLAYER_START_Y
playerxchange=0

# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0,screen_width))
    enemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyY_change.append(ENEMY_SPEED_Y)
    #Game loop

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
       if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

