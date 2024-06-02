import pygame
from pygame.locals import * 
import random 

pygame.init()

clock = pygame.time.Clock()
fps = 60

screen_width = 864 
screen_height = 936 

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# define game variables 
ground_scroll = 0
scroll_speed = 4

# load images 
bg = pygame.image.load("img/bg.png")
ground_img = pygame.image.load("img/ground.png")


class Bird(pygame.sprite.sprite):
    def __init__(self, x, y): 
        pygame.sprite.sprite.__init__(self)
        self.image = pygame.image.load("img/bird1.png")
        self.rect = self.image.get_rect()  
        self.rect.center = [x, y]

# almost like a python list (list of sprites)
bird_group = pygame.sprite.Group()

flappy = Bird(100, int(screen_height / 2)) 

bird_group.add(flappy)

run = True 
while run: 

    # use the clock / fps 
    clock.tick(fps)

    # draw background 
    screen.blit(bg, (0,0))

    bird_group.draw(screen)

    # draw ground and make it scroll 
    screen.blit(ground_img, (ground_scroll, 768))
    ground_scroll -= scroll_speed
    if abs(ground_scroll) > 35: 
        ground_scroll = 0
    
    # how to exit the game 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()
    

pygame.quit()

