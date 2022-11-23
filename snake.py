 import pygame
import sys
import random
import time

pygame.init()
pygame.display.set_caption('Snake game by Novak Evgeniy')
sc = pygame.display.set_mode((1200, 675))
sc.fill((0, 0, 255))
snake_size = 1
snake_squares = []
snake_x = 600
snake_y = 338
speed_x = 0
speed_y = 0
bonus_x = 300
bonus_y = 400
f1 = pygame.font.Font(None, 50)
text1 = f1.render('THE GREATEST GSELIK SNAKE', True,
                  (180, 0, 0))

f2 = pygame.font.SysFont('serif', 48)
text3 = f2.render("easy", False,
                  (0, 180, 0))
f2 = pygame.font.SysFont('serif', 48)
text4 = f2.render("medium", False,
                  (255, 255, 0))
f2 = pygame.font.SysFont('serif', 48)
text5 = f2.render("hard", False,
                  (255, 102, 0))
f2 = pygame.font.SysFont('serif', 48)
text6 = f2.render("extreme", False,
                  (128, 0, 0))
f2 = pygame.font.SysFont('serif', 48)
text7 = f2.render("impossible", False,
                  (0, 0, 0))


reasy = pygame.Rect(550, 165, 80, 60)
pygame.draw.rect(sc, (0, 0, 255), reasy, 0)
rmedium = pygame.Rect(510, 275, 160, 60)
pygame.draw.rect(sc, (0, 0, 255), rmedium, 0)
rhard = pygame.Rect(550, 385, 85, 60)
pygame.draw.rect(sc, (0, 0, 255), rhard, 0)
rextreme = pygame.Rect(510, 495, 160, 60)
pygame.draw.rect(sc, (0, 0, 255), rextreme, 0)
rinsane = pygame.Rect(480, 605, 220, 60)
pygame.draw.rect(sc, (0, 0, 255), rinsane, 0)

clock = pygame.time.Clock()
snake_speed = 0

sc.blit(text1, (350, 50))
sc.blit(text3, (550, 160))
sc.blit(text4, (510, 270))
sc.blit(text5, (550, 380))
sc.blit(text6, (510, 490))
sc.blit(text7, (490, 600))
u = 0
pygame.display.update()
while True:
    if u == 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= 550 and event.pos[0] <= 630 and event.pos[1] >= 165 and event.pos[1] <= 225:
                snake_speed = 40
                u = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= 510 and event.pos[0] <= 670 and event.pos[1] >= 275 and event.pos[1] <= 335:
                snake_speed = 80
                u = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= 550 and event.pos[0] <= 635 and event.pos[1] >= 385 and event.pos[1] <= 445:

                snake_speed = 120
                u = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= 510 and event.pos[0] <= 670 and event.pos[1] >= 495 and event.pos[1] <= 555:
                snake_speed = 180
                u = 1
            if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] >= 480 and event.pos[0] <= 700 and event.pos[1] >= 605 and event.pos[1] <= 665:
                snake_speed = 500
                u = 1


    if u == 1:
        if (snake_x >= 1200 or snake_x < 0 or snake_y >= 675 or snake_y < 0):
            u = 2
        for x in snake_squares[:-1]:
            if x == snake_head:
                u = 2
        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_squares.append(snake_head)
        if len(snake_squares) > snake_size:
            del snake_squares[0]
        sc.fill((0, 0, 255))
        pygame.draw.rect(sc, (255, 0, 0), [snake_x, snake_y, 10, 10])
        pygame.draw.rect(sc, (0, 214, 120), [bonus_x, bonus_y, 10, 10])
        for block in snake_squares:
            pygame.draw.rect(sc, (255, 0, 0), [block[0], block[1], 10, 10])
        clock.tick(snake_speed)
        snake_x += speed_x
        snake_y += speed_y
        if abs(snake_x - bonus_x) < 10 and abs(snake_y - bonus_y) < 10:
            snake_size += 1
            bonus_x = random.randrange(0, 1190)
            bonus_y = random.randrange(0, 665)
            snake_speed += 2
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and speed_y != 2:
                    speed_x = 0
                    speed_y = -2

                if event.key == pygame.K_DOWN and speed_y != -2:
                    speed_x = 0
                    speed_y = 2

                if event.key == pygame.K_LEFT and speed_x != 2:
                    speed_y = 0
                    speed_x = -2

                if event.key == pygame.K_RIGHT and speed_x != -2:
                    speed_y = 0
                    speed_x = 2

    if u == 2:
        pygame.display.flip()
        sc.fill((0, 0, 255))
        font = pygame.font.SysFont('Arial', 100)
        score = font.render('You scored ' + str(snake_size-1), True, (255, 0, 0))
        sc.blit(score, (340, 308))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()



