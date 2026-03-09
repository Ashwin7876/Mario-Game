import pygame 
# Initialize Pygame
pygame.init()

clock = pygame.time.Clock()


# Set up the game window
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Hello Pygame")
player_speed=5
sprites = pygame.sprite.Group()
# Game loop
mario=pygame.sprite.Sprite(sprites)
mario.image = pygame.image.load("mario.png")
mario.image=pygame.transform.scale(mario.image,(50,50))
mario.rect = mario.image.get_rect()
pygame.transform.scale(screen,(50,50))

running = True

bg = pygame.image.load(".mario_background.png")

#INSIDE OF THE GAME LOOP
screen.blit(bg, (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        mario.rect.x -= player_speed
    if keys[pygame.K_RIGHT]:
        mario.rect.x += player_speed
    if keys[pygame.K_UP]:
        mario.rect.y -= player_speed   # up = minus
    if keys[pygame.K_DOWN]:
        mario.rect.y += player_speed   # down = plus

    screen.blit(bg, (0, 0))

    # screen.blit(mario, mario_rect)
    sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()