import enemy
import tower
import objective
import const
import imports
import pygame as pg


pg.init()


screen = pg.display.set_mode((const.WIDTH, const.HEIGHT))
pg.display.set_caption("Tower Defense")

fps = const.FPS
spawn_rate = const.SPAWN_RATE

enemies = []
towers = []

clock = pg.time.Clock()
running = True
money = 10


def select_panel():
    pg.draw.rect(screen, const.GRAY, (0, 0, const.PANEL_HEIGHT, const.HEIGHT))
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
        button_rect = pg.Rect(10, y_offset, const.PANEL_HEIGHT - 20, 50)
        pg.draw.rect(screen, color, button_rect)
        
        # Display tower info
        text = font.render(f"{tower_type.capitalize()} - Cost: {cost}", True, const.BLACK)
        screen.blit(text, (20, y_offset + 15))
        
        # Check if this button is clicked
        if pg.mouse.get_pressed()[0] and button_rect.collidepoint(pg.mouse.get_pos()):
            global selected_tower_type
            selected_tower_type = tower_type
            print(f"Selected tower type: {selected_tower_type}")
        
        y_offset += 70


while running:
    screen.fill(const.BLACK)

    for event in pg.event.get():
        if event == pg.QUIT:
            running = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if x > const.PANEL_HEIGHT and selected_tower_type:
                tower_info = const.TOWER_TYPE[selected_tower_type]
                if money >= tower_info["cost"]:
                    try:
                        towers.append(tower.Tower(selected_tower_type, x, y))  # Instantiate tower
                        money -= tower_info["cost"]
                        print(f"Placed {selected_tower_type} tower at ({x}, {y})")  # Debugging line
                        selected_tower_type = None
                    except Exception as e:
                        print(f"Error while creating tower: {e}")  # Error message for troubleshooting

    spawn_rate -= 1
    if spawn_rate == 0:
        type = imports.random.randint(1, 3)
        enemies.append(enemy.Enemy(const.ENEMY_ID[type]))
        spawn_rate == const.SPAWN_RATE


    for enemy in enemies[:]:
        enemy.move()
        enemy.draw(screen)
        if enemy.x < const.PANEL_HEIGHT:
            enemies.remove(enemy)
        elif enemy.health <= 0:
            enemies.remove(enemy)
            money += 1  # Reward for defeating enemy

    # Update and draw towers
    for tower in towers:
        tower.attack(enemies)
        tower.draw(screen)

    select_panel()

    pg.display.flip()
    clock.tick(fps)

pg.quit()



