player = Player()
enemies = pygame.sprite.Group()
for i in range(8):
    enemies.add(Enemy(x=random.randint(0, 760)))

all_sprites = pygame.sprite.Group(player, *enemies)

# in the game loop:
all_sprites.update()          # calls update() on every sprite
all_sprites.draw(screen)      # blits every image at its rect
