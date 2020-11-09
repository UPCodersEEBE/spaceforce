import pygame

darker = (34, 30, 49)
dark = (65, 72, 93)
light = (119, 142, 152)
lighter = (197, 219, 212)
outline = (255, 255, 239)


class Moon(pygame.sprite.Sprite):
    # This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, screen, x, y, rad, moon_img):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # resize sprite
        moon_img = pygame.transform.scale(moon_img, (2 * rad, 2 * rad))

        # Draw the brick (a rectangle!)
        pygame.draw.circle(screen, outline, (x, y), rad + 1)
        pygame.draw.circle(screen, lighter, (x, y), rad)
        # screen.blit(moon_img, (x - rad, y - rad))
