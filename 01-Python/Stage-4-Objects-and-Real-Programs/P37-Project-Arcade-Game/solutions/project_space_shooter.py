import random
import pygame

W, H = 800, 600
pygame.init()
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Space Shooter")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28)
big = pygame.font.SysFont("arial", 64, bold=True)


def ship_surface(colour, flip=False):
    s = pygame.Surface((40, 30), pygame.SRCALPHA)
    pts = [(20, 0), (40, 30), (20, 22), (0, 30)]
    if flip:
        pts = [(x, 30 - y) for x, y in pts]
    pygame.draw.polygon(s, colour, pts)
    return s


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = ship_surface((80, 200, 255))
        self.rect = self.image.get_rect(midbottom=(W // 2, H - 20))
        self.cooldown = 0

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 7
        self.rect.clamp_ip(screen.get_rect())
        self.cooldown = max(0, self.cooldown - 1)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, vy, colour):
        super().__init__()
        self.image = pygame.Surface((4, 12))
        self.image.fill(colour)
        self.rect = self.image.get_rect(center=pos)
        self.vy = vy

    def update(self):
        self.rect.y += self.vy
        if self.rect.bottom < 0 or self.rect.top > H:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, level):
        super().__init__()
        self.image = ship_surface((240, 90, 90), flip=True)
        self.rect = self.image.get_rect(center=(random.randint(30, W - 30), -20))
        self.vy = random.uniform(1.5, 2.5) + level * 0.3
        self.vx = random.choice([-2, -1, 1, 2])

    def update(self):
        self.rect.y += self.vy
        self.rect.x += self.vx
        if self.rect.left < 0 or self.rect.right > W:
            self.vx = -self.vx
        if self.rect.top > H:
            self.kill()


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((4, 4))
        self.image.fill(random.choice([(255, 200, 0), (255, 120, 0), (255, 255, 255)]))
        self.rect = self.image.get_rect(center=pos)
        self.v = [random.uniform(-4, 4), random.uniform(-4, 4)]
        self.life = random.randint(15, 30)

    def update(self):
        self.rect.x += self.v[0]
        self.rect.y += self.v[1]
        self.life -= 1
        if self.life <= 0:
            self.kill()


def load_high():
    try:
        with open("shooter_high.txt") as f:
            return int(f.read())
    except (FileNotFoundError, ValueError):
        return 0


def new_game():
    g = {"player": Player(), "bullets": pygame.sprite.Group(), "enemy_bullets": pygame.sprite.Group(),
         "enemies": pygame.sprite.Group(), "particles": pygame.sprite.Group(),
         "score": 0, "lives": 3, "frames": 0, "shake": 0}
    return g


state, high, g = "menu", load_high(), None
stars = [(random.randint(0, W), random.randint(0, H)) for _ in range(80)]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN and state != "playing":
                g, state = new_game(), "playing"
            elif event.key == pygame.K_p and state in ("playing", "paused"):
                state = "paused" if state == "playing" else "playing"
            elif event.key == pygame.K_SPACE and state == "playing" and g["player"].cooldown == 0:
                g["bullets"].add(Bullet(g["player"].rect.midtop, -10, (255, 255, 120)))
                g["player"].cooldown = 10

    offset = (0, 0)
    if state == "playing":
        g["frames"] += 1
        level = g["frames"] // 900
        if random.random() < 0.02 + level * 0.006:
            g["enemies"].add(Enemy(level))
        for e in g["enemies"]:
            if random.random() < 0.004:
                g["enemy_bullets"].add(Bullet(e.rect.midbottom, 6, (255, 80, 80)))
        for grp in ("player", "bullets", "enemy_bullets", "enemies", "particles"):
            g[grp].update()

        for enemy in pygame.sprite.groupcollide(g["enemies"], g["bullets"], True, True):
            g["score"] += 10
            g["particles"].add(*[Particle(enemy.rect.center) for _ in range(20)])
        if (pygame.sprite.spritecollide(g["player"], g["enemies"], True)
                or pygame.sprite.spritecollide(g["player"], g["enemy_bullets"], True)):
            g["lives"] -= 1
            g["shake"] = 15
            g["particles"].add(*[Particle(g["player"].rect.center) for _ in range(30)])
            if g["lives"] == 0:
                high = max(high, g["score"])
                with open("shooter_high.txt", "w") as f:
                    f.write(str(high))
                state = "over"
        if g["shake"]:
            g["shake"] -= 1
            offset = (random.randint(-6, 6), random.randint(-6, 6))

    screen.fill((5, 5, 20))
    for i, (sx, sy) in enumerate(stars):
        stars[i] = (sx, (sy + 1 + i % 3) % H)
        screen.set_at(stars[i], (200, 200, 255))
    if g:
        for grp in ("particles", "bullets", "enemy_bullets", "enemies"):
            for s in g[grp]:
                screen.blit(s.image, s.rect.move(offset))
        if state != "over":
            screen.blit(g["player"].image, g["player"].rect.move(offset))
        hud = f"Score {g['score']}   Lives {g['lives']}   Best {high}"
        screen.blit(font.render(hud, True, (255, 255, 255)), (10, 10))
    if state == "menu":
        screen.blit(big.render("SPACE SHOOTER", True, (255, 255, 255)), (165, 200))
        screen.blit(font.render("Arrows move · SPACE fires · P pauses · ENTER to start", True, (180, 180, 220)), (110, 300))
    elif state == "paused":
        screen.blit(big.render("PAUSED", True, (255, 255, 255)), (290, 250))
    elif state == "over":
        screen.blit(big.render("GAME OVER", True, (240, 90, 90)), (230, 220))
        screen.blit(font.render("ENTER to play again", True, (255, 255, 255)), (280, 310))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
