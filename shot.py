import pygame
import circleshape

class Shot(circleshape.CircleShape):
    # Static field for group containers
    containers = None

    # Initializer
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Automatically add the shot to all specified groups
        if Shot.containers:
            for group in Shot.containers:
                group.add(self)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)