import random
import pygame

W, H = 800, 600
pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

def new_star(z=None):
    return [random.uniform(-W, W), random.uniform(-H, H), z or random.uniform(1, W)]

stars = [new_star() for _ in range(400)]
speed = 8
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        speed = min(40, speed + 0.5)
    if keys[pygame.K_DOWN]:
        speed = max(1, speed - 0.5)

    screen.fill((0, 0, 0))
    for s in stars:
        s[2] -= speed
        if s[2] <= 1:
            s[:] = new_star(W)
        sx = W / 2 + s[0] / s[2] * 200
        sy = H / 2 + s[1] / s[2] * 200
        if 0 <= sx < W and 0 <= sy < H:
            size = max(1, int(4 * (1 - s[2] / W)))
            b = int(255 * (1 - s[2] / W))
            pygame.draw.circle(screen, (b, b, b), (int(sx), int(sy)), size)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
