import pygame
import sys
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60  # Reduced FPS for slower time progression
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Run")

background_image = pygame.image.load("forest.png")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

girl_image = pygame.image.load("girl1.png")
girl_image = pygame.transform.scale(girl_image, (50, 50))

monster_image = pygame.image.load("monster2.png")
monster_image = pygame.transform.scale(monster_image, (75, 75))

player_size = 50
player_speed = 5

monster_size = 50
monster_speed = 5

player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 20

lives = 3
current_player_image = girl_image

clock = pygame.time.Clock()

monsters = []

font = pygame.font.Font(None, 36)

# Track the start time
start_time = pygame.time.get_ticks()

while lives > 0:
    # Calculate elapsed time
    elapsed_time = (pygame.time.get_ticks() - start_time) / 1000  # Convert milliseconds to seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    if random.randint(0, 100) < 5:
        monster_x = random.randint(0, WIDTH - monster_size)
        monster_y = 0
        monsters.append([monster_x, monster_y])

    for monster in monsters:
        monster[1] += monster_speed

    for monster in monsters:
        if (
            player_x < monster[0] + monster_size
            and player_x + player_size > monster[0]
            and player_y < monster[1] + monster_size
            and player_y + player_size > monster[1]
        ):
            lives -= 1
            print(f"Remaining Lives: {lives}")
            monsters = []
            pygame.time.delay(1000)

            # Change the player character image after each loss of life
            if lives == 2:
                current_player_image = pygame.image.load("boy1.png")
                current_player_image = pygame.transform.scale(current_player_image, (50, 50))
            elif lives == 1:
                current_player_image = pygame.image.load("girl1.png")
                current_player_image = pygame.transform.scale(current_player_image, (50, 50))

    monsters = [monster for monster in monsters if monster[1] < HEIGHT]

    screen.blit(background_image, (0, 0))

    for monster in monsters:
        screen.blit(monster_image, (monster[0], monster[1]))

    screen.blit(current_player_image, (player_x, player_y))

    # Displaying remaining lives on the screen
    lives_text = font.render(f"Lives: {lives}", True, WHITE)
    screen.blit(lives_text, (10, 10))

    # Display elapsed time
    time_text = font.render(f"Time: {int(elapsed_time)}s", True, WHITE)
    screen.blit(time_text, (10, 50))

    pygame.display.flip()

    clock.tick(FPS)

    # Check for win condition
    if elapsed_time >= 180:  # 180 seconds = 3 minutes
        break

# Game over at the end
if lives > 0:
    game_over_text = font.render("You Win!!! :D", True, WHITE)
else:
    game_over_text = font.render("Game Over!!! XD", True, WHITE)

screen.blit(game_over_text, (WIDTH // 2 - 100, HEIGHT // 2 - 18))
pygame.display.flip()

pygame.time.delay(3000)
pygame.quit()
sys.exit()




