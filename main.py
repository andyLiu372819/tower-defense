import enemy
import tower
import const
import imports
import pygame as pg
import sys


pg.init()


screen = pg.display.set_mode((const.WIDTH, const.HEIGHT))
pg.display.set_caption("Tower Defense")

fps = const.FPS
spawn_rate = const.SPAWN_RATE
spawn_timer = spawn_rate

enemies = []
towers = []

clock = pg.time.Clock()
running = True
up_timer = const.INCREASE_DIFF_RATE
money = 20

selected_tower_type = None


def select_panel():
    global selected_tower_type
    pg.draw.rect(screen, const.GRAY, (0, 0, const.PANEL_WIDTH, const.HEIGHT))
    font = pg.font.SysFont(None, 24)

    # Display player currency
    currency_text = font.render(f"Currency: {money}", True, const.BLACK)
    screen.blit(currency_text, (10, 10))

    # Tower selection buttons
    y_offset = 50
    for tower_type in const.TOWER_TYPE:
        tower_info = const.TOWER_TYPE[tower_type]
        color = tower_info["color"]
        cost = tower_info["cost"]

        # Draw button rectangle
        button_rect = pg.Rect(10, y_offset, const.PANEL_WIDTH - 20, 50)
        pg.draw.rect(screen, color, button_rect)

        if selected_tower_type == tower_type:
            pg.draw.rect(screen, const.BLUE, button_rect, 5)

        # Display tower info
        text = font.render(f"{tower_type.capitalize()} - Cost: {cost}", True, const.BLACK)
        screen.blit(text, (20, y_offset + 15))
        
        # Check if this button is clicked
        if pg.mouse.get_pressed()[0] and button_rect.collidepoint(pg.mouse.get_pos()):
            selected_tower_type = tower_type
        
        y_offset += 50

    
    quit_button =  pg.Rect(10, 700, const.PANEL_WIDTH - 20, 50)
    pg.draw.rect(screen, const.WHITE, quit_button)

    tt = font.render(f"QUIT", True, const.RED)
    screen.blit(tt, (20, 715))
    
    if pg.mouse.get_pressed()[0] and quit_button.collidepoint(pg.mouse.get_pos()):
        pg.quit()


def restart():
    global enemies, towers, spawn_timer, spawn_rate, money
    enemies = []
    towers = []
    spawn_rate = const.SPAWN_RATE
    spawn_timer = spawn_rate
    money = 20


def paused():
    p = True
    font = pg.font.SysFont(None, 120)

    text = font.render(f"PAUSED", True, const.RED)
    screen.blit(text, (450, 350))

    while p:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
        
        new_font = pg.font.SysFont(None, 24)

        cont_button = pg.Rect(250, 600, 100, 50)
        quit_button = pg.Rect(850, 600, 100, 50)
        restart_button = pg.Rect(600, 600, 100, 50)
        pg.draw.rect(screen, const.WHITE, cont_button)
        pg.draw.rect(screen, const.WHITE, quit_button)
        pg.draw.rect(screen, const.WHITE, restart_button)

        cont_text = new_font.render("CONTINUE", True, const.GREEN)
        quit_text = new_font.render("QUIT", True, const.RED)
        restart_text = new_font.render("RESTART", True, const.BLUE)

        screen.blit(cont_text, (260, 610))
        screen.blit(quit_text, (860, 610))
        screen.blit(restart_text, (610, 610))

        if pg.mouse.get_pressed()[0]:
            if quit_button.collidepoint(pg.mouse.get_pos()):
                pg.quit()
            elif cont_button.collidepoint(pg.mouse.get_pos()):
                p = False
            elif restart_button.collidepoint(pg.mouse.get_pos()):
                restart()
                p = False
                

        pg.display.update()

def check_defeat():
    global enemies
    for i in enemies:
        if i.x < const.PANEL_WIDTH:
            print("lost")
            return True
    return False

def defeated():
    defeat = check_defeat()
    font = pg.font.SysFont(None, 96)
    while defeat:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()

        text = font.render(f"YOU LOST", True, const.RED)
        screen.blit(text, (450, 350))

        new_font = pg.font.SysFont(None, 24)

        cont_button = pg.Rect(250, 600, 100, 50)
        quit_button = pg.Rect(850, 600, 100, 50)
        pg.draw.rect(screen, const.WHITE, cont_button)
        pg.draw.rect(screen, const.WHITE, quit_button)

        cont_text = new_font.render("RESTART", True, const.GREEN)
        quit_text = new_font.render("QUIT", True, const.RED)

        screen.blit(cont_text, (260, 610))
        screen.blit(quit_text, (860, 610))

        if pg.mouse.get_pressed()[0]:
            if quit_button.collidepoint(pg.mouse.get_pos()):
                pg.quit()
            elif cont_button.collidepoint(pg.mouse.get_pos()):
                restart()
                defeat = False

        pg.display.update()

def spawn():
    global spawn_rate, enemies, spawn_timer
    if spawn_timer <= 0:
        type = imports.random.randint(1, 100)
        if type < 70:
            enemies.append(enemy.Enemy(const.ENEMY_ID[1]))
        elif type < 90:
            enemies.append(enemy.Enemy(const.ENEMY_ID[2]))
        else:
            enemies.append(enemy.Enemy(const.ENEMY_ID[3]))
        spawn_timer = spawn_rate
    else:
        spawn_timer = spawn_timer - 1

def increase():
    global up_timer, spawn_rate
    if up_timer == 0:
        spawn_rate = spawn_rate * 0.9
        up_timer = const.INCREASE_DIFF_RATE
    else:
        up_timer -= 1

while running:
    screen.fill(const.BLACK)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if x > const.PANEL_WIDTH and selected_tower_type:
                tower_info = const.TOWER_TYPE[selected_tower_type]
                if money >= tower_info["cost"]:
                    try:
                        towers.append(tower.Tower(selected_tower_type, x, y))  # Instantiate tower
                        money -= tower_info["cost"]
                    except Exception as e:
                        print(f"Error while creating tower: {e}")  # Error message for troubleshooting
            else:
                print("Tower not selected")
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                paused()
    
    spawn()
    defeated()
    increase()

    for i in enemies:
        i.move()
        i.attack(towers, screen)
        i.draw(screen)
        if i.health <= 0:
            enemies.remove(i)
            money += i.money  # Reward for defeating enemy

    # Update and draw towers
    for i in towers:
        i.attack(enemies, screen)
        i.draw(screen)
        if i.health <= 0:
            towers.remove(i)

    select_panel()

    pg.display.flip()
    clock.tick(fps)


pg.quit()