import pygame
import random

GREEN=(0, 255, 0)
RED=(255,0,0)
BLACK=(0,0,0,)
WHITE=(255,255,255)

window_x = 1000
window_y = 1000
game_window = pygame.display.set_mode((window_x, window_y))

clock = pygame.time.Clock()
fps = 60

pygame.init() 
pygame.joystick.init()
pygame.display.set_caption('Snake')
game_window = pygame.display.set_mode((window_x, window_y))

direction = 'RIGHT'
Snake_pos = [500, 500]
Snake = [[500, 500]]
apple = [random.randrange(0, window_x-9, 10), random.randrange(0, window_y-9, 10)]
apples_eaten = 0

running = True
check_for_collision = False

def score(apples_eaten):
    font = pygame.font.SysFont('Comic Sans MS', 50)
    score_surface = font.render('Score: ' + str(apples_eaten), True, (255,255,255))
    score_rect = score_surface.get_rect()
    game_window.blit(score_surface, score_rect)


while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    joystick_count = pygame.joystick.get_count()
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        axes = joystick.get_numaxes()
        for i in range(axes):
            axis = joystick.get_axis(i)
            print(axis)
            if i == 0:
                if axis > 0.0:
                    direction = 'RIGHT'
                if axis < 0.0:
                    direction = 'LEFT'
            if i == 1:
                if axis > 0.0:
                    direction = 'DOWN'
                if axis < 0.0:
                    direction = 'UP'

    
    if direction == 'RIGHT':
        Snake_pos[0] += 10
    elif direction == 'LEFT':
        Snake_pos[0] -= 10
    elif direction == 'UP':
        Snake_pos[1] -= 10
    elif direction == 'DOWN':
        Snake_pos[1] += 10

    game_window.fill(BLACK)
    Snake.insert(0, list(Snake_pos))
    if Snake_pos[0] == apple[0] and Snake_pos[1] == apple[1]:
        apple = [random.randrange(0, window_x+1, 10), random.randrange(0, window_y+1, 10)]
        apples_eaten += 1
        check_for_collision = True
    else:
        Snake.pop()

    if check_for_collision == True:
        for i in range(len(Snake)):
            if i == 0:
                i = 1
            if Snake_pos == Snake[i]:
                running = False

    if Snake_pos[0] <= -1:
        Snake_pos[0] = 1000
    elif Snake_pos[0] >= 1001:
        Snake_pos[0] = 0
    if Snake_pos[1] <= -1:
        Snake_pos[1] = 1000
    elif Snake_pos[1] >= 1001:
        Snake_pos[1] = 0

    for snek in Snake:
        pygame.draw.rect(game_window, GREEN, (snek[0], snek[1], 10, 10))
    pygame.draw.rect(game_window, RED, (apple[0], apple[1], 10, 10))

    score(apples_eaten)
    pygame.display.update()





#amogus   
if direction == 'RIGHT':
    Snake_pos[0] += 10
elif direction == 'LEFT':
    Snake_pos[0] -= 10
elif direction == 'UP':
    Snake_pos[1] -= 10
elif direction == 'DOWN':
    Snake_pos[1] += 10

