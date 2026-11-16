import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():      # 1. events
        if event.type == pygame.QUIT:
            running = False

    # 2. update (nothing yet)

    screen.fill((30, 30, 40))             # 3. draw
    pygame.draw.circle(screen, (255, 200, 0), (400, 300), 50)
    pygame.display.flip()
    clock.tick(60)                        # 60 FPS

pygame.quit()
