import pygame
import random

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800, 600))

# Title and Icon
pygame.display.set_caption("Pong")
icon = pygame.image.load('pong_icon.png')
pygame.display.set_icon(icon)

# Player
player_width = 15
player_height = 80
player_x = 20
player_y = (600 - player_height) // 2
player_vel = 0

# Enemy
enemy_width = 15
enemy_height = 80
enemy_x = 780
enemy_y = (600 - enemy_height) // 2
enemy_vel = 0

# Ball
ball_width = 15
ball_height = 15
ball_x = 400
ball_y = 300
ball_vel_x = random.randint(-8, 8) if random.randint(0, 1) == 0 else random.randint(-8, -1)
ball_vel_y = random.randint(-8, 8) if random.randint(0, 1) == 0 else random.randint(-8, -1)

# Score
player_score = 0
enemy_score = 0

# Game loop
running = True
while running:
    # RGB
    screen.fill((0, 0, 0))

    # Player
    pygame.draw.rect(screen, (255, 255, 255), (player_x, player_y, player_width, player_height))

    # Enemy
    pygame.draw.rect(screen, (255, 255, 255), (enemy_x, enemy_y, enemy_width, enemy_height))

    # Ball
    pygame.draw.rect(screen, (255, 255, 255), (ball_x, ball_y, ball_width, ball_height))

    # Score
    font = pygame.font.Font('freesansbold.ttf', 32)
    player_text = font.render(f"{player_score}", True, (255, 255, 255))
    enemy_text = font.render(f"{enemy_score}", True, (255, 255, 255))
    screen.blit(player_text, (350, 10))
    screen.blit(enemy_text, (450, 10))

    # Movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_vel = -5
            if event.key == pygame.K_DOWN:
                player_vel = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player_vel = 0

    # Enemy AI
    if enemy_y + enemy_height // 2 < ball_y + ball_height // 2:
        enemy_vel = 3
    elif enemy_y + enemy_height // 2 > ball_y + ball_height // 2:
        enemy_vel = -3
    else:
        enemy_vel = 0

    # Player movement
    player_y += player_vel
    if player_y <= 0:
        player_y = 0
    elif player_y + player_height >= 600:
        player_y = 600 - player_height

    # Enemy movement
    enemy_y += enemy_vel
    if enemy_y <= 0:
        enemy_y = 0
    elif enemy_y + enemy_height >= 600:
        enemy_y = 600 - enemy_height

    # Ball movement
    ball_x += ball_vel_x
    ball_y += ball_vel_y

    # Collision
    if ball_x <= player_x + player_width:
        if ball_y + ball_height >= player_y and ball_y <= player_y + player_height:
            ball_vel_x = -ball_vel_x
            ball_vel_y = random.randint(-8, 8) if random.randint(0, 1) == 0 else random.randint(-8, -1)
    elif ball_x + ball_width >= enemy_x:
        if ball_y + ball_height >= enemy_y and ball_y <= enemy_y + enemy_height:
            ball_vel_x = -ball_vel_x
            ball_vel_y = random.randint(-8, 8) if random.randint(0, 1) == 0 else random.randint(-8, -1)

    # Wall collision
    if ball_y <= 0:
        ball_vel_y = -ball_vel_y
    elif ball_y + ball_height >= 600:
        ball_vel_y = -ball_vel_y

    # Score
    if ball_x <= 0:
        enemy_score += 1
        ball_x = 400
        ball_y = 300
        ball_vel_x = random.randint(-8, 8) if random.randint(0, 1) == 0 else random.randint(-8, -1)
        ball_vel_y = random.randint(-8, 8) if random.randint(0, 1) == 0 else random.randint(-8, -1)
    elif ball_x + ball_width >= 800:
        player_score += 1
        ball_x = 400
        ball_y = 300
        ball_vel_x = random.randint(-7, 7) if random.randint(0, 1) == 0 else random.randint(-7, -1)
        ball_vel_y = random.randint(-7, 7) if random.randint(0, 1) == 0 else random.randint(-7, -1)

    pygame.display.update()