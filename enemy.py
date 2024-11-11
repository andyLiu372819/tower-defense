import imports
import const
from const import ENEMY_TYPES as et


class Enemy:

    def __init__(self, type):
        self.type = type
        self.radius = et[type]["radius"]
        self.health, self.max_health = et[type]["health"], et[type]["health"]
        self.colour = et[type]["colour"]
        self.x = imports.const.WIDTH
        self.y = imports.random.randint(50, imports.const.HEIGHT - 50)
        self.speed = 1

    def move(self):
        self.x -= self.speed

    def draw(self, screen):
        imports.pygame.draw.circle(screen, self.colour, (self.x, self.y), self.radius)

        hbar_width = self.radius * 2
        h_ratio = self.health / self.max_health
        hb_x = self.x - self.radius
        hb_y = self.y - self.radius - 5

        imports.pygame.draw.rect(screen, const.RED, (hb_x, hb_y, hbar_width, 5))
        imports.pygame.draw.rect(screen, const.DARK_GREEN, (hb_x, hb_y, hbar_width * h_ratio, 5))