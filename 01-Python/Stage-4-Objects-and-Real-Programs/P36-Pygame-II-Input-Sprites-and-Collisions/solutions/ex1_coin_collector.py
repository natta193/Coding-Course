import random
import pygame

W, H = 800, 600
pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28)

player = pygame.Rect(380, 280, 40, 40)
coins = [pygame.Rect(random.randint(20, W - 40), random.randint(20, H - 40), 20, 20) for _ in range(10)]
score = 0
start = pygame.time.get_ticks()
finished_time = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    player.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 5
    player.y += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * 5
    player.clamp_ip(screen.get_rect())

    for c in coins[:]:
        if player.colliderect(c):
            coins.remove(c)
            score += 1
    if not coins and finished_time is None:
        finished_time = (pygame.time.get_ticks() - start) / 1000

    screen.fill((25, 25, 35))
    for c in coins:
        pygame.draw.ellipse(screen, (255, 215, 0), c)
    pygame.draw.rect(screen, (0, 200, 255), player)
    elapsed = finished_time or (pygame.time.get_ticks() - start) / 1000
    msg = f"Score {score}/10   Time {elapsed:.1f}s" + ("   YOU WIN!" if finished_time else "")
    screen.blit(font.render(msg, True, (255, 255, 255)), (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
