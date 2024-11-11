WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (200, 200, 200)


ENEMY_TYPES = {
    "Soldier": {"radius": 5, "health": 100, "colour": RED},
    "Centurion": {"radius": 10, "health": 300, "colour": (255, 100, 100)},
    "General": {"radius": 20, "health": 600, "colour": YELLOW}
}


ENEMY_ID = {
    1: "Soldier",
    2: "Centurion",
    3: "General"
}


TOWER_TYPE = {
    "Guard": {"damage": 50, "rate": 2, "cost": 2, "color": GREEN, "range": 10},
    "Archer": {"damage": 150, "rate": 1, "cost": 4, "color": BLUE, "range": 150},
    "Crossbow": {"damage": 60, "rate": 4, "cost": 6, "color": WHITE, "range": 100}
}


TOWER_ID = {
    1: "Guard",
    2: "Archer",
    3: "Crossbow"
}


FPS = 60

WIDTH, HEIGHT = 1200, 800
PANEL_HEIGHT = 200

SPAWN_RATE = 5
