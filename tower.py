import imports
from const import TOWER_TYPE as tt


class Tower:

    def __init__(self, type, x, y):
        print(f"Initializing tower of type: {type}")
        self.type = type
        if self.type in ["Archer", "Crossbow"]:
            self.ranged = True
        self.damage = tt[type]["damage"]
        self.rate = tt[type]["rate"]
        self.cost = tt[type]["cost"]
        self.color = tt[type]["color"]
        self.range = tt[type]["range"]
        self.x = x
        self.y = y
        self.timer = 0

    def attack(self, enemies, screen):
        if self.timer == 0:
            for enemy in enemies:
                dist = imports.math.hypot(enemy.x - self.x, enemy.y - self.y)
                if dist <= self.range: 
                    enemy.health -= self.damage
                    self.timer = self.rate

                    if self.ranged:
                        imports.pygame.draw.line(screen, self.color, (self.x, self.y), (enemy.x, enemy.y), 2)
                    break
        else:
            self.timer -= 1
        
    def draw(self, screen):
        if self.type == "Crossbow":
            imports.pygame.draw.polygon(screen, self.color, [(self.x, self.y - 10), (self.x - 10, self.y + 10), (self.x + 10, self.y + 10)])
        elif self.type == "Guard":
            imports.pygame.draw.rect(screen, self.color, (self.x - 10, self.y - 10, 20, 20))
        elif self.type == "Archer":
            imports.pygame.draw.polygon(screen, self.color, [
                (self.x + 10, self.y),
                (self.x + 5, self.y - 10),
                (self.x - 5, self.y - 10),
                (self.x - 10, self.y),
                (self.x - 5, self.y + 10),
                (self.x + 5, self.y + 10),
            ])