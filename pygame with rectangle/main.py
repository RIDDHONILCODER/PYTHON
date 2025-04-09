import pygame 

pygame.init()

screen=pygame.display.set_mode((300,400))

done=False

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pygame.draw.rect(screen,(0,100,200),pygame.Rect(20,20,100,200))
    pygame.display.flip()