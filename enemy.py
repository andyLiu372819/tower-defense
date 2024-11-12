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
        self.range = et[type]["range"]
        self.damage = et[type]["damage"]
        self.rate = et[type]["rate"]
        self.speed = 1
        self.timer = 0

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
    
    def attack(self, towers, screen):
        if self.timer == 0:
            attacked, index = False, 0
            while not attacked:
                tower = towers[index]
                dist = imports.math.hypot(self.x - tower.x, self.y - tower.y)

                if dist <= self.range:
                    tower.health -= self.damage
                    self.speed = 0
                    
                    imports.pygame.draw.line(screen, self.colour, (self.x, self.y), (tower.x, tower.y), 2)

                    attacked = True
                    self.timer = self.rate
            
            if not attacked:
                self.speed = 1
            
            
        else:
            self.timer -= 1
