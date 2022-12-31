import pygame

# Initialize pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the title
pygame.display.set_caption("Click Jump Game")

# Set up the player sprite
player_image = pygame.image.load("player.png")
player_sprite = pygame.sprite.Sprite()
player_sprite.image = player_image
player_sprite.rect = player_image.get_rect()
player_sprite.rect.centerx = window_size[0] // 2
player_sprite.rect.bottom = window_size[1]

# Set up the floor sprite
floor_image = pygame.image.load("floor.png")
floor_sprite = pygame.sprite.Sprite()
floor_sprite.image = floor_image
floor_sprite.rect = floor_image.get_rect()
floor_sprite.rect.bottom = window_size[1]

# Set up the background
background_image = pygame.image.load("background.png")
background_rect = background_image.get_rect()

# Set the player's starting speed
player_speed = 0

# Set the gravity
gravity = 1

# Set the jump strength
jump_strength = 15

# Set the game clock
clock = pygame.time.Clock()

# Set the game loop flag
running = True

# Game loop
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            player_speed = -jump_strength

    # Update the player's speed
    player_speed += gravity

    # Update the player's position
    player_sprite.rect.bottom += player_speed

    # Check for collision with the floor
    if player_sprite.rect.colliderect(floor_sprite.rect):
        player_sprite.rect.bottom = floor_sprite.rect.top
        player_speed = 0

    # Draw the background
    screen.blit(background_image, background_rect)

    # Draw the player
    screen.blit(player_sprite.image, player_sprite.rect)

    # Draw the floor
    screen.blit(floor_sprite.image, floor_sprite.rect)

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Quit pygame
pygame.quit()



