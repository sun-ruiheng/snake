import pygame
from snake import *

pygame.init()
bounds = (800, 500)
screen = pygame.display.set_mode(bounds)

block_size = 20
snake = Snake(block_size, bounds)

pygame.display.set_caption("Snake")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

running = True
while running:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        snake.steer(Direction.UP)
    elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
        snake.steer(Direction.DOWN)
    elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
        snake.steer(Direction.LEFT)
    elif keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        snake.steer(Direction.RIGHT)
    snake.move()

    screen.fill((0, 0, 80))
    snake.draw(pygame, screen)
    pygame.display.update() #or flip()
