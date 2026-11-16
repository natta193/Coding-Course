import random
import pygame

W, H = 800, 600
pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()


def rand_colour():
    return random.randint(80, 255), random.randint(80, 255), random.randint(80, 255)


class Bouncer:
    def __init__(self):
        self.rect = pygame.Rect(100, 100, 120, 60)
        self.vx, self.vy = 3, 2
        self.colour = rand_colour()

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left <= 0 or self.rect.right >= W:
            self.vx = -self.vx
            self.colour = rand_colour()
        if self.rect.top <= 0 or self.rect.bottom >= H:
            self.vy = -self.vy
            self.colour = rand_colour()

    def draw(self, surf):
        pygame.draw.rect(surf, self.colour, self.rect, border_radius=12)


class Particle:
    def __init__(self, x, y, colour, vx, vy, life):
        self.x, self.y, self.colour, self.vx, self.vy, self.life = x, y, colour, vx, vy, life
        self.max_life = life

    def update(self):
        self.vy += 0.08
        self.x += self.vx
        self.y += self.vy
        self.life -= 1

    def draw(self, surf):
        f = self.life / self.max_life
        c = tuple(int(v * f) for v in self.colour)
        pygame.draw.circle(surf, c, (int(self.x), int(self.y)), 3)


class Fireworks:
    def __init__(self):
        self.rockets = []
        self.sparks = []

    def update(self):
        if random.random() < 0.04:
            self.rockets.append(Particle(random.randint(100, W - 100), H, (255, 255, 255), 0, random.uniform(-11, -8), 60))
        for r in self.rockets[:]:
            r.update()
            if r.vy >= -1:
                self.rockets.remove(r)
                col = rand_colour()
                for _ in range(40):
                    self.sparks.append(Particle(r.x, r.y, col, random.uniform(-4, 4), random.uniform(-4, 4), random.randint(30, 60)))
        for s in self.sparks:
            s.update()
        self.sparks = [s for s in self.sparks if s.life > 0]

    def draw(self, surf):
        for p in self.rockets + self.sparks:
            p.draw(surf)


class Snow:
    def __init__(self):
        self.flakes = [[random.randint(0, W), random.randint(0, H), random.uniform(1, 3)] for _ in range(200)]

    def update(self):
        for f in self.flakes:
            f[1] += f[2]
            f[0] += random.uniform(-0.5, 0.5)
            if f[1] > H:
                f[0], f[1] = random.randint(0, W), 0

    def draw(self, surf):
        for x, y, s in self.flakes:
            pygame.draw.circle(surf, (230, 230, 255), (int(x), int(y)), int(s))


effects = {pygame.K_1: Bouncer(), pygame.K_2: Fireworks(), pygame.K_3: Snow()}
current = effects[pygame.K_1]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
        elif event.type == pygame.KEYDOWN and event.key in effects:
            current = effects[event.key]
    current.update()
    screen.fill((0, 0, 0))
    current.draw(screen)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
