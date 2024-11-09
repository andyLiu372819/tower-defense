import imports
from const import ENEMY_TYPES as et


class Enemy:

    def __init__(self, type):
        self.type = type
        self.radius = et[type]["radius"]
        self.health = et[type]["health"]
        self.colour = et[type]["colour"]
        self.x = imports.const.WIDTH
        self.y = imports.random.randint(50, imports.const.HEIGHT - 50)
        self.speed = 1

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        imports.pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)