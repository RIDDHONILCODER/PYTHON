import pygame
pygame.init()
screen=pygame.display.set_mode((300,400))
final=False

bg_image=pygame.image.load("bg.png")
bg_image=pygame.transform.scale(bg_image.convert(),(300,400))

while not final:
    clock=pygame.time.Clock()
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
    screen.blit(bg_image,(0,0))
    pygame.display.flip()
    clock.tick(30)
    pygame.quit()

