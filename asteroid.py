import pygame
import random
import circleshape
import constants

class Asteroid(circleshape.CircleShape):
    # Static field for group containers
    containers = None

    # Initializer
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

        # Automatically add the asteroid to all specified groups
        if Asteroid.containers:
            for group in Asteroid.containers:
                group.add(self)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)
    
    def split(self):
        # Check the size of the asteroid
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            self.kill() # Small asteroid, just kill
        
        # Generate a random angle between 20 and 50 degrees
        random_angle = random.uniform(20, 50)

        # Create new velocity vectors rotated by random_angle and -random_angle
        new_velocity_1 = self.velocity.rotate(random_angle) * 1.2
        new_velocity_2 = self.velocity.rotate(-random_angle) * 1.2

        # Calculate the new radius
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS

        # Create two new Asteroids at the current position
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Set their velocities
        asteroid_1.velocity = new_velocity_1
        asteroid_2.velocity = new_velocity_2

        # Kill the current asteroid
        self.kill()

        # Add the new asteroids to the relevant groups
        if Asteroid.containers:
            for group in Asteroid.containers:
                group.add(asteroid_1)
                group.add(asteroid_2)
