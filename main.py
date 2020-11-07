import pygame
import math
from moon import Moon

pygame.init()

pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 30)

WHITE1 = (255, 255, 255)
WHITE2 = (190, 190, 190)
WHITE3 = (45, 45, 45)
BLACK = (0, 0, 0)
LIGHTBLUE = (0, 176, 240)

x, y = 000, 500
vx, vy = 1, 0

screen_width, screen_height = 800, 600
scaling_factor = 1

pygame.init()
win = pygame.display.set_mode(
    (screen_width * scaling_factor, screen_height * scaling_factor)
)
screen = pygame.Surface((screen_width, screen_height))

# (x,y,radi)
all_moons = [(240, 400, 20), (240, 601, 30)]


def get_forces():
    fx = 0
    fy = -1
    stop = False
    for moon in all_moons:
        ax = moon[0] - x
        ay = moon[1] - y
        m = 3.14159256536 * 4 * moon[2] ** 3 / 30
        f = m * 10 / (ax ** 2 + ay ** 2)
        o = math.atan(ay / ax)
        fx += f * abs(math.cos(o)) * ax / abs(ax)
        fy += f * abs(math.sin(o)) * ay / abs(ay)
        if abs(ay) < moon[2] and abs(ax) < moon[2]:
            stop = True
    return fx, fy, stop


run = True
while run:
    pygame.time.delay(16)

    fx, fy, stop = get_forces()

    if stop == False:
        vx += fx / 10
        vy += fy / 10
        x += vx
        y += vy

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= 20
    if keys[pygame.K_RIGHT]:
        x += 20
    if keys[pygame.K_UP]:
        y -= 20
    if keys[pygame.K_DOWN]:
        y += 20

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.fill(BLACK)

    for i in all_moons:
        Moon(screen, i[0], i[1], i[2])
    pygame.draw.rect(screen, (0, 100, 255), (x, y, 5, 5))

    win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))
    win.blit(screen, myfont.render("Some Text", False, (0, 0, 0)), (0, 0))
    pygame.display.update()
pygame.quit()