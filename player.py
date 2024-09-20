import pygame
import constants
import circleshape
import shot

class Player(circleshape.CircleShape):
    # Static field for group containers
    containers = None

    # Initializer
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.timer = 0

        # Automatically add the player to all specified groups
        if Player.containers:
            for group in Player.containers:
                group.add(self)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
        
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += (constants.PLAYER_TURN_SPEED * dt)
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += (forward * constants.PLAYER_SPEED * dt)
    
    def update(self, dt):
        self.timer -= dt

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer <= 0:
            self.timer = constants.PLAYER_SHOOT_COOLDOWN
            new_shot = shot.Shot(self.position.x, self.position.y, constants.SHOT_RADIUS)
            new_shot.velocity = (pygame.Vector2(0, 1).rotate(self.rotation) * constants.PLAYER_SHOOT_SPEED)

            if shot.Shot.containers:
                for group in shot.Shot.containers:
                    group.add(new_shot)
