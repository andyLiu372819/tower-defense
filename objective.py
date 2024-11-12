import imports
import const


def fail(enemies):
    for enemy in enemies:
        if enemy.x < const.PANEL_WIDTH:
            return True
        
    return False