import pygame
from moon import Moon
import random
from functions.physics import generate_moons, get_forces

pygame.init()
font = pygame.font.SysFont("8-Bit-Madness", 35, True, False)


darker = (34, 30, 49)
dark = (65, 72, 93)
light = (119, 142, 152)
lighter = (197, 129, 212)
outline = (255, 255, 239)

x, y = 0, 0
vx, vy = 0, 0
rad = 8
av = 0.2
maxv = 5

nmoon = 5

screen_width, screen_height = 240, 160
scaling_factor = 4

win = pygame.display.set_mode(
    (screen_width * scaling_factor, screen_height * scaling_factor)
)
screen = pygame.Surface((screen_width, screen_height))

ship = pygame.image.load("./assets/ship.png").convert_alpha()
dock = pygame.image.load("./assets/dock.png").convert_alpha()
moon_img = pygame.image.load("./assets/moon4.png").convert_alpha()
# (x,y,radi)


all_moons = generate_moons(nmoon, rad)

stars = []
for i in range(80):
    stars.append([random.random() * screen_width, random.random() * screen_height])


camera = 0
run = True
while run:
    screen.fill(darker)
    pygame.time.delay(50)
    fx, fy, stop = get_forces(all_moons, x, y, rad)
    camera += 0.1
    if camera > screen_width:
        camera = 0
    if stop:
        vx, vy = 0, 0
    else:
        vx = min(fx + vx, maxv)
        vy = min(fy + vy, maxv)
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
    if keys[pygame.K_r]:
        x, y = 0, 0
        vx, vy = 0, 0
        all_moons = generate_moons(nmoon, rad)
    if keys[pygame.K_w]:
        x, y = 0, 0
        vx, vy = 0, 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for i in stars:
        pygame.draw.rect(
            screen,
            outline,
            (i[0] - camera, i[1], 1, 1),
        )
        pygame.draw.rect(
            screen,
            outline,
            (i[0] - camera + screen_width, i[1], 1, 1),
        )
    screen.blit(ship, (x - rad, y - rad))
    for i in all_moons:
        Moon(screen, i[0], i[1], i[2], moon_img)
    screen.blit(dock, (208, 87))
    win.blit(pygame.transform.scale(screen, win.get_rect().size), (0, 0))
    text = font.render("x: " + str(int(x)) + "y: " + str(int(y)), 5, (255, 255, 255))
    # win.blit(text, (10, 10))
    pygame.display.update()
pygame.quit()