import pygame 

pygame.init()

screen=pygame.display.set_mode((300,400))

done=False
x=20
y=20
width=100
height=200

clock=pygame.time.Clock()  

while not done:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            done=True
    pressed=pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        x -=3
    if pressed[pygame.K_RIGHT]:
        x +=3
    if pressed[pygame.K_UP]:
        y -=3    
    if pressed[pygame.K_DOWN]:
        y +=3    
    screen.fill((0,0,0))
    pygame.draw.rect(screen,(0,100,200),pygame.Rect(x,y,width,height))
    pygame.display.flip()
    clock.tick(90)

    