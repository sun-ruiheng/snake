import pygame
from snake import *
from food import Food

pygame.init()
bounds = (800, 500)
screen = pygame.display.set_mode(bounds)

block_size = 20
snake = Snake(block_size, bounds)
food = Food(block_size, bounds)

font = pygame.font.SysFont('dejavuserif', 65, True)

pygame.display.set_caption("Snake")
icon = pygame.image.load('snake.png')
pygame.display.set_icon(icon)

running = True
while running:
    pygame.time.delay(60)

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
    snake.check_for_food(food)
    if snake.check_bounds() or snake.check_tail_collision():
        text = font.render('Game Over', True, (255, 255, 255))
        screen.blit(text, (200, 120))
        text2 = font.render('Score: ' + str(snake.length), True, (255, 255, 255))
        screen.blit(text2, (200, 200))
        text2 = font.render('Restarting...', True, (255, 255, 255))
        screen.blit(text2, (200, 280))
        pygame.display.update()
        pygame.time.delay(2000)
        snake.respawn()
        food.respawn()

    screen.fill((0, 0, 80))
    snake.draw(pygame, screen)
    food.draw(pygame, screen)
    pygame.display.update() #or flip()
