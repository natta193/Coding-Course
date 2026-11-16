import random
import pygame

W, H = 800, 600

class Ball:
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.vx = random.uniform(-5, 5)
        self.vy = random.uniform(-8, 0)
        self.r = random.randint(10, 30)
        self.colour = [random.randint(80, 255) for _ in range(3)]

    def update(self):
        self.vy += 0.4
        self.x += self.vx
        self.y += self.vy
        if self.x < self.r or self.x > W - self.r:
            self.vx = -self.vx
            self.x = max(self.r, min(W - self.r, self.x))
        if self.y > H - self.r:
            self.y = H - self.r
            self.vy = -self.vy * 0.8

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, (int(self.x), int(self.y)), self.r)

pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
balls = []
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            balls.append(Ball(*event.pos))
    for b in balls:
        b.update()
    screen.fill((20, 20, 30))
    for b in balls:
        b.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
