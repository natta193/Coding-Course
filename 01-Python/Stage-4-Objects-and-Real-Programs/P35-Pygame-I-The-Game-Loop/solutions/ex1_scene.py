import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Scene")
clock = pygame.time.Clock()
clouds = [[100, 80], [400, 130], [650, 60]]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for c in clouds:
        c[0] += 1
        if c[0] > 900:
            c[0] = -100

    screen.fill((135, 206, 235))
    pygame.draw.circle(screen, (255, 220, 0), (700, 100), 50)
    for cx, cy in clouds:
        for dx in (0, 30, 60):
            pygame.draw.circle(screen, (255, 255, 255), (cx + dx, cy), 30)
    pygame.draw.rect(screen, (60, 170, 60), (0, 450, 800, 150))
    pygame.draw.rect(screen, (200, 120, 80), (300, 330, 180, 130))
    pygame.draw.polygon(screen, (150, 40, 40), [(280, 330), (390, 250), (500, 330)])
    pygame.draw.rect(screen, (90, 50, 20), (370, 400, 40, 60))
    for tx in (120, 620):
        pygame.draw.rect(screen, (100, 60, 20), (tx - 10, 380, 20, 80))
        pygame.draw.circle(screen, (30, 130, 40), (tx, 360), 45)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
