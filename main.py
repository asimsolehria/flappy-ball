import random

import pygame
from pygame.locals import *

pygame.init()
width = 1000
height = 530
size = (width, height)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Ball")
ipipe = pygame.image.load("sprites/pipe.bmp")
pipe = pygame.transform.rotate(ipipe, 180)
ball = pygame.image.load("sprites/small-ball.bmp")
font = pygame.font.SysFont(None, 50)


def message_to_screen(msg, color, x, y):
    screen_text = font.render(msg, True, color)
    screen.blit(screen_text, [x, y])


def game_loop():
    upperX = [x for x in range(250, width + 1, 250)]
    upperY = []
    for i in range(4):
        upperY.append(random.randrange(-10, -300, -20))

    ballx = 100
    bally = 0
    ballgravity = 1

    running = True
    gameOver = False

    while running:
        while gameOver == True:
            screen.blit(pygame.image.load("sprites/game-over.bmp"), [0, 0])
            message_to_screen("Game Over! Press P to play or Q to quit", (255, 0, 0), 100, height - 100)
            message_to_screen("Use space key to control the falling ball", (255, 255, 255), 100, 30)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    gameOver = False
                elif event.type == KEYDOWN:
                    if event.key == K_p:
                        game_loop()
                    elif event.key == K_q:
                        running = False
                        gameOver = False

        pygame.time.Clock().tick(30)

        ballgravity += 1
        bally += ballgravity

        for e in pygame.event.get():
            if e.type == QUIT:
                running = False
            elif e.type == KEYDOWN and e.key == K_SPACE:
                ballgravity = 0
                bally -= 50
        if bally + ball.get_height() // 2 > height or bally < 0:
            gameOver = True

        screen.fill((255, 255, 0))
        screen.blit(ball, [ballx, bally])
        for i in range(4):
            screen.blit(pipe, [upperX[i], upperY[i]])
            screen.blit(ipipe, [upperX[i], upperY[i] + 500])
        for i in range(len(upperX)):
            upperX[i] -= 4
        if upperX[0] < -(pipe.get_width()):
            upperX.pop(0)
            upperX.append(1000)
            upperY.pop(0)
            upperY.append(random.randrange(-10, -300, -20))
        pygame.display.update()
    pygame.quit()


game_loop()
