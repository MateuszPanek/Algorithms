from random import randint

import pygame
import os

pygame.init()
window_height = 600
window_width = 600
screen = pygame.display.set_mode((window_height, window_width))


def screen_text_items(text, x, y, size):
    font = pygame.font.SysFont('Helvetica', size)
    render = font.render(text, 1, (255, 100, 100))
    screen.blit(render, (x, y))


current_display = 'Menu'


class Obstacle:

    def __init__(self, obstacle_x, obstacle_width):
        self.obstacle_x = obstacle_x
        self.obstacle_width = obstacle_width
        self.obstacle_y_top = 0
        self.obstacle_height_top = randint(150, 250)
        self.gap = 200

        self.obstacle_y_bottom = self.obstacle_height_top + self.gap
        self.obstacle_height_bottom = window_height - self.obstacle_y_bottom
        self.obstacle_colour = (160, 140, 190)
        self.obstacle_top = pygame.Rect(self.obstacle_x, self.obstacle_y_top,
                                        self.obstacle_width, self.obstacle_height_top)
        self.obstacle_bottom = pygame.Rect(self.obstacle_x, self.obstacle_y_bottom,
                                           self.obstacle_width, self.obstacle_height_bottom)

    def obstacles_print(self):
        pygame.draw.rect(screen, self.obstacle_colour, self.obstacle_top, 0)
        pygame.draw.rect(screen, self.obstacle_colour, self.obstacle_bottom, 0)

    def movement(self, v):
        self.obstacle_x = self.obstacle_x - v
        self.obstacle_top = pygame.Rect(self.obstacle_x, self.obstacle_y_top,
                                        self.obstacle_width, self.obstacle_height_top)
        self.obstacle_bottom = pygame.Rect(self.obstacle_x, self.obstacle_y_bottom,
                                           self.obstacle_width, self.obstacle_height_bottom)
    # TODO --> fix collision, they are not working properly - something might be wrong with the calculation
    def collision(self, player):
        if self.obstacle_top.colliderect(player) or self.obstacle_bottom.colliderect(player):
            print('Przywaliłeś w przeszkodę !')
            return True
        else:
            return False

class Helicopter:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.height = 30
        self.width = 50
        self.shape = pygame.Rect(self.x, self.y, self.height, self.width)
        self.graphics = pygame.image.load(os.path.join('heli.png'))

    def draw_heli(self):
        screen.blit(self.graphics, (self.x, self.y))

    def heli_movement(self, v):
        self.y = self.y + v

    def heli_speed(self, v):
        self.x = self.x + v

player = Helicopter(250,275)
heli_direction = 0
heli_speed = 0
obstacles = []

for i in range(21):
    obstacles.append(Obstacle(i * window_width / 20, window_width / 20))


while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                heli_direction = -2
            if event.key == pygame.K_DOWN:
                heli_direction = 2
            if event.key == pygame.K_SPACE:
                if current_display != 'Game':
                    player = Helicopter(250, 275)
                    heli_direction = 0
                    current_display = 'Game'
            if event.key == pygame.K_RIGHT:
                heli_speed = 1
            if event.key == pygame.K_LEFT:
                heli_speed = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                heli_speed = 0
            if event.key == pygame.K_LEFT:
                heli_speed = 0
            if event.key == pygame.K_UP:
                heli_direction = 0
            if event.key == pygame.K_DOWN:
                heli_direction = 0
    screen.fill((0, 0, 0))
    if current_display == 'Menu':
        screen_text_items('Press space to start', 80, 300, 40)
        menu_graphics = pygame.image.load(os.path.join('logo.png'))
        screen.blit(menu_graphics, (80, 30))
    elif current_display == 'Game':
        for obstacle in obstacles:
            obstacle.movement(1)
            obstacle.obstacles_print()
            if obstacle.collision(player.shape):
                current_display == 'End'
                screen_text_items('Sorry, you have lost', 80, 400, 40)
                end_graphics = pygame.image.load(os.path.join('logo.png'))
                screen.blit(end_graphics, (80, 30))



        for obstacle in obstacles:
            if obstacle.obstacle_x <= -obstacle.obstacle_width:
                obstacles.remove(obstacle)
                obstacles.append((Obstacle(window_width, window_width / 20)))


    player.draw_heli()
    player.heli_movement(heli_direction)
    player.heli_speed(heli_speed)
    pygame.display.update()

