import pygame 
# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()

# Set up the game window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello Pygame")
player_speed=5
# Game loop
mario = pygame.transform.scale(pygame.image.load("mario-2d.png"), (50, 50))
mario_rect = mario.get_rect()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        mario_rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        mario_rect.x += player_speed
    if keys[pygame.K_UP]:
        mario_rect.y -= player_speed   # up = minus
    if keys[pygame.K_DOWN]:
        mario_rect.y += player_speed   # down = plus

    screen.fill("purple")
    screen.blit(mario, mario_rect)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()