import pygame
import random

pygame.init()

screen_width,screen_height=500,400

font_size=72
# Load and transform the background image

background_image = pygame.transform.scale(pygame.image.load("bg.jpg"),(screen_width,screen_height))

# Load font once at the beginning

font = pygame.font.SysFont("Times New Roman", font_size)

class Sprite(pygame.sprite.Sprite):
    def __init__(self,color,height,width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue')) # Background color of sprite
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        self.rect = self.image.get_rect()
    def move(self,xchange,ychange):
        self.rectx=max(min(self.rect.x + xchange, screen_width - self.rect.width), 0)
        self.rect.y=max(min(self.rect.y + ychange, screen_height - self.rect.height), 0)

screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("sprite colision")

all_Sprite=pygame.sprite.Group()
sprite1=Sprite(pygame.Color("black"),20,30)
sprite1.rect.x=random.randint(0,screen_width)
sprite1.rect.y=random.randint(0,screen_height)
all_Sprite.add(sprite1)

sprite2=Sprite(pygame.Color("red"),20,30)
sprite2.rect.x=random.randint(0,screen_width)
sprite2.rect.y=random.randint(0,screen_height)
all_Sprite.add(sprite2)

running, won = True, False
clock = pygame.time.Clock()

# Main game loop
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                     and event.key == pygame.K_x):
      running = False

  if not won:
    keys = pygame.key.get_pressed()
    x_change = (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 72
    y_change = (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 72
    sprite1.move(x_change, y_change)

    if sprite1.rect.colliderect(sprite2.rect):
      all_Sprite.remove(sprite2)
      won = True

  # Drawing
  screen.blit(background_image, (0, 0))
  all_Sprite.draw(screen)

  # Display win message
  if won:
    win_text = font.render("You win!", True, pygame.Color('black'))
    screen.blit(win_text, ((screen_width - win_text.get_width()) // 2,
                           (screen_height - win_text.get_height()) // 2))

  pygame.display.flip()
  clock.tick(90)

pygame.quit()



