import pygame


class Player(pygame.sprite.Sprite):
    # This class represents a brick. It derives from the "Sprite" class in Pygame.

    def __init__(self, screen, x, y, rad):
        # Call the parent class (Sprite) constructor
        super().__init__()

        # Draw the brick (a rectangle!)
        pygame.draw.circle(screen, (ball_color), (x, y), rad)
