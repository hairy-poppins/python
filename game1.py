import pygame
from pygame.locals import *
import random
import sys

# pygame setup
pygame.init()
vec = pygame.math.Vector2  # 2 for two dimensional
HEIGHT = 600
WIDTH = 1280
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()


        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.acc.x = -0.5
        if keys[pygame.K_RIGHT]:
            self.acc.x = 0.5
        if keys[pygame.K_UP]:
            self.acc.y = -0.5
        if keys[pygame.K_DOWN]:
            self.acc.y = 0.5

        # apply friction
        self.acc.x += self.vel.x * -0.1
        self.acc.y += self.vel.y * -0.1
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc  # dt is 1

        # wrap around the sides of the screen
        if self.pos.x > 1280:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = 1280
        if self.pos.y > 600:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = 600

        self.rect.midbottom = self.pos

class Food(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((10, 10))
        self.surf.fill((255,0,0))
    def spawn(self):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(0, HEIGHT)
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        

P1 = Player()
f1 = Food()
f1.spawn()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(f1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    displaysurface.fill((0,0,0))
	
    
    P1.move()
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
    
    pygame.display.update()

    clock.tick(60)  # limits FPS to 60

pygame.quit()