import pygame
import math
from moon import Moon

pygame.init()
font = pygame.font.SysFont("8-Bit-Madness", 15, True, False)


WHITE1 = (255, 255, 255)
WHITE2 = (190, 190, 190)
WHITE3 = (45, 45, 45)
EXPLOSION = (200, 20, 20)
BLACK = (0, 0, 0)
LIGHTBLUE = (0, 176, 240)
ball_color = LIGHTBLUE

x, y = 000, 50
vx, vy = 0, 5
rad = 3
av = 2

screen_width, screen_height = 240, 160
scaling_factor = 4

pygame.init()
win = pygame.display.set_mode(
    (screen_width * scaling_factor, screen_height * scaling_factor)
)
screen = pygame.Surface((screen_width, screen_height))

# (x,y,radi)
all_moons = [(240, 40, 20), (100, 130, 30)]


def get_forces():
    fx = 0
    fy = 0
    stop = False
    for moon in all_moons:
        ax = moon[0] - x
        ay = moon[1] - y
        m = 1 * moon[2] ** 3 / 30
        f = m * 10 / (ax ** 2 + ay ** 2)
        o = math.atan(ay / ax)
        fx += f * abs(math.cos(o)) * ax / abs(ax)
        fy += f * abs(math.sin(o)) * ay / abs(ay)
        if abs(ay) - rad < moon[2] and abs(ax) - rad < moon[2]:
            stop = True
    return fx, fy, stop


run = True
while run:
    pygame.time.delay(100)
    fx, fy, stop = get_forces()

    if stop:
        vx, vy = 0, 0
        rad += 1
        ball_color = EXPLOSION
        if rad >= 15:
            run = False
            rad = 0
    else:
        vx += fx
        vy += fy
        x += vx
        y += vy

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        vx -= av
    if keys[pygame.K_RIGHT]:
        vx += av
    if keys[pygame.K_UP]:
        vy -= av
    if keys[pygame.K_DOWN]:
        vy += av

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(BLACK)

    for i in all_moons:
        Moon(screen, i[0], i[1], i[2])

    pygame.draw.circle(screen, ball_color, (x, y), rad)
    win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))
    # text = font.render("Highscore: ", 2, (255, 255, 255))
    # win.blit(text, (10, 10))
    pygame.display.update()
pygame.quit()