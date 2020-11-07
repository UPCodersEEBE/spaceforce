import pygame

BLACK = (0, 0, 0)


class Moon(pygame.sprite.Sprite):
    # This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, screen, x, y, rad):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Draw the brick (a rectangle!)
        pygame.draw.circle(screen, (50, 50, 50), (x, y), rad + 1)
        pygame.draw.circle(screen, (200, 200, 200), (x, y), rad)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), rad - 1)
