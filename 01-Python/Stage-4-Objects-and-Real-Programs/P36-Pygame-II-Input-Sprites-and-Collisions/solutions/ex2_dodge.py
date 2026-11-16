import random
import pygame

W, H = 800, 600

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill((0, 200, 255))
        self.rect = self.image.get_rect(midbottom=(W // 2, H - 20))

    def update(self):
        keys = pygame.key.get_pressed()
        self.rect.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 7
        self.rect.clamp_ip(pygame.Rect(0, 0, W, H))

class Block(pygame.sprite.Sprite):
    def __init__(self, speed):
        super().__init__()
        size = random.randint(20, 50)
        self.image = pygame.Surface((size, size))
        self.image.fill((230, 60, 60))
        self.rect = self.image.get_rect(midbottom=(random.randint(0, W), 0))
        self.speed = speed * random.uniform(0.7, 1.3)

    def update(self):
        self.rect.y += self.speed
        if self.rect.top > H:
            self.kill()

def load_high():
    try:
        with open("dodge_high.txt") as f:
            return float(f.read())
    except (FileNotFoundError, ValueError):
        return 0.0

pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 32)
big = pygame.font.SysFont("arial", 64, bold=True)

state = "menu"
high = load_high()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and state != "playing":
            player = Player()
            blocks = pygame.sprite.Group()
            all_sprites = pygame.sprite.Group(player)
            start = pygame.time.get_ticks()
            state = "playing"

    screen.fill((20, 20, 30))
    if state == "menu":
        screen.blit(big.render("DODGE!", True, (255, 255, 255)), (300, 200))
        screen.blit(font.render("Press SPACE to start", True, (200, 200, 200)), (265, 300))
    elif state == "playing":
        survived = (pygame.time.get_ticks() - start) / 1000
        if random.random() < 0.04 + survived / 600:
            b = Block(4 + survived / 5)
            blocks.add(b)
            all_sprites.add(b)
        all_sprites.update()
        if pygame.sprite.spritecollideany(player, blocks):
            score = survived
            if score > high:
                high = score
                with open("dodge_high.txt", "w") as f:
                    f.write(str(high))
            state = "over"
        all_sprites.draw(screen)
        screen.blit(font.render(f"{survived:.1f}s", True, (255, 255, 255)), (10, 10))
    elif state == "over":
        screen.blit(big.render("GAME OVER", True, (230, 60, 60)), (230, 180))
        screen.blit(font.render(f"You lasted {score:.1f}s   Best {high:.1f}s", True, (255, 255, 255)), (220, 280))
        screen.blit(font.render("SPACE to play again", True, (200, 200, 200)), (270, 340))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
