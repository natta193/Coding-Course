# two rectangles overlapping?
if player.rect.colliderect(coin.rect):
    score += 1

# player vs a whole group (True = remove the hit ones)
hits = pygame.sprite.spritecollide(player, enemies, True)
if hits:
    lives -= 1

# group vs group: bullets hit enemies, both removed
pygame.sprite.groupcollide(bullets, enemies, True, True)
