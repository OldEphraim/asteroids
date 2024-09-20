import pygame
import constants
import player
import asteroid
import asteroidfield
import shot

def main():
    pygame.init()
    
    # Set up display
    screen = pygame.display.set_mode((constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # Create a clock object to manage FPS
    clock = pygame.time.Clock()

    # Initialize delta time (dt) variable
    dt = 0

    # Creating groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Set the static field for containers
    player.Player.containers = (updatable, drawable)
    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = (updatable)
    shot.Shot.containers = (shots, updatable, drawable)

    # Create a player object (triangle)
    triangle = player.Player(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2)

    # Create an asteroid field object
    field = asteroidfield.AsteroidField()

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
        # Fill the screen with black
        screen.fill((0, 0, 0))
        
        # Handle updating
        for shape in updatable:
            shape.update(dt)

        # Handle player colliding with asteroid
        for asteroid_shape in asteroids:
            if triangle.collides_with(asteroid_shape):
                print("Game over!")
                running = False
                break

        # Handle shot colliding with asteroid
        for bullet in shots:
            for asteroid_shape in asteroids:
                if bullet.collides_with(asteroid_shape):
                    bullet.kill()
                    asteroid_shape.split()
                    break
        
        # Handle drawing
        for shape in drawable:
            shape.draw(screen)

        # Update the display
        pygame.display.flip()

        # Cap the frame rate at 60 FPS and get the delta time (in seconds)
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

pygame.quit()