import pygame

# Initialize required modules

pygame.init

# Initialize required modules

pygame.init()

# Setup window geometry

screen = pygame.display.set_mode((300,400))

finished=False

while not finished:
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
        