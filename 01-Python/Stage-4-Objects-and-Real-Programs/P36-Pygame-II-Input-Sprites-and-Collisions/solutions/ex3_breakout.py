import pygame

W, H = 800, 600
pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 28)

paddle = pygame.Rect(W // 2 - 50, H - 40, 100, 14)
ball = pygame.Rect(W // 2, H // 2, 14, 14)
vx, vy = 4, -5
bricks = [pygame.Rect(20 + c * 76, 60 + r * 28, 70, 22) for r in range(6) for c in range(10)]
COLOURS = [(230, 60, 60), (240, 140, 40), (240, 220, 60), (80, 200, 90), (60, 160, 230), (150, 90, 220)]
lives, score = 3, 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    paddle.x += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * 8
    paddle.clamp_ip(screen.get_rect())

    if lives > 0 and bricks:
        ball.x += vx
        ball.y += vy
        if ball.left <= 0 or ball.right >= W:
            vx = -vx
        if ball.top <= 0:
            vy = -vy
        if ball.colliderect(paddle) and vy > 0:
            offset = (ball.centerx - paddle.centerx) / 50     # -1 .. 1
            vx = offset * 7
            vy = -abs(vy)
        hit = ball.collidelist(bricks)
        if hit != -1:
            bricks.pop(hit)
            vy = -vy
            score += 10
        if ball.top > H:
            lives -= 1
            ball.center = (W // 2, H // 2)
            vx, vy = 4, -5

    screen.fill((15, 15, 25))
    for b in bricks:
        pygame.draw.rect(screen, COLOURS[(b.y - 60) // 28], b)
    pygame.draw.rect(screen, (220, 220, 220), paddle)
    pygame.draw.ellipse(screen, (255, 255, 255), ball)
    status = f"Score {score}   Lives {lives}"
    if not bricks:
        status += "   YOU WIN!"
    elif lives == 0:
        status += "   GAME OVER"
    screen.blit(font.render(status, True, (255, 255, 255)), (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
