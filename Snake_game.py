import pygame
from random import randrange

RES = 800
SIZE = 20

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'A': True, 'S': True, 'D': True}
length = 1
snake = [(x, y)]
dx, dy = 0, 0
fps = 20
score = 0

pygame.init()
sc = pygame.display.set_mode([RES, RES])
clock = pygame.time.Clock()
font_score = pygame.font.SysFont('Times New Roman', 20, bold = True)

while True:
    sc.fill(pygame.Color('black'))

    [(pygame.draw.rect(sc, pygame.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pygame.draw.rect(sc, pygame.Color('red'), (*apple, SIZE, SIZE))

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('white'))
    sc.blit(render_score, (5, 5))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-length:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        length += 1
        score += 1
        fps += 0.125

    if x < 0:
        x = RES
    if x > RES:
        x = 0
    if y < 0:
        y = RES
    if y > RES:
        y = 0

    if len(snake) != len(set(snake)):
        break

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    pygame.display.flip()
    clock.tick(fps)

    key = pygame.key.get_pressed()

    if key[pygame.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'A': True, 'S': False, 'D': True}

    if key[pygame.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'A': True, 'S': True, 'D': False}

    if key[pygame.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'A': True, 'S': True, 'D': True}

    if key[pygame.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'A': False, 'S': True, 'D': True}