x, y = 100, 300
vx, vy = 4, 3                 # velocity (pixels per frame)

while running:
    # ... events ...
    x += vx
    y += vy
    if x < 20 or x > 780:     # bounce off walls
        vx = -vx
    if y < 20 or y > 580:
        vy = -vy

    screen.fill((30, 30, 40))
    pygame.draw.circle(screen, (255, 200, 0), (x, y), 20)
    pygame.display.flip()
    clock.tick(60)
