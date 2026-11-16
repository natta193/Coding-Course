import random
import pygame

W, H = 800, 500
pygame.init()
screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 48, bold=True)
small = pygame.font.SysFont("arial", 24)

left = pygame.Rect(30, H // 2 - 50, 12, 100)
right = pygame.Rect(W - 42, H // 2 - 50, 12, 100)
ball = pygame.Rect(W // 2 - 8, H // 2 - 8, 16, 16)
vx, vy = 5, 3
scores = [0, 0]
state = "menu"
ai = False


def reset_ball(direction):
    global vx, vy
    ball.center = (W // 2, H // 2)
    vx, vy = 5 * direction, random.choice([-3, -2, 2, 3])


running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN and state != "playing" and e.key in (pygame.K_SPACE, pygame.K_1):
            ai = e.key == pygame.K_1
            scores = [0, 0]
            reset_ball(random.choice([-1, 1]))
            state = "playing"

    if state == "playing":
        k = pygame.key.get_pressed()
        left.y += (k[pygame.K_s] - k[pygame.K_w]) * 7
        if ai:
            if ball.centery > right.centery + 15:
                right.y += 5
            elif ball.centery < right.centery - 15:
                right.y -= 5
        else:
            right.y += (k[pygame.K_DOWN] - k[pygame.K_UP]) * 7
        left.clamp_ip(screen.get_rect())
        right.clamp_ip(screen.get_rect())

        ball.x += vx
        ball.y += vy
        if ball.top <= 0 or ball.bottom >= H:
            vy = -vy
        for paddle, direction in ((left, 1), (right, -1)):
            if ball.colliderect(paddle) and vx * direction < 0:
                offset = (ball.centery - paddle.centery) / 50
                vx = -vx * 1.05
                vy = offset * 6
        if ball.right < 0:
            scores[1] += 1
            reset_ball(-1)
        elif ball.left > W:
            scores[0] += 1
            reset_ball(1)
        if max(scores) >= 7:
            state = "over"

    screen.fill((10, 10, 20))
    for y in range(0, H, 30):
        pygame.draw.rect(screen, (60, 60, 80), (W // 2 - 2, y, 4, 15))
    pygame.draw.rect(screen, (255, 255, 255), left)
    pygame.draw.rect(screen, (255, 255, 255), right)
    pygame.draw.ellipse(screen, (255, 220, 0), ball)
    screen.blit(font.render(f"{scores[0]}   {scores[1]}", True, (255, 255, 255)), (W // 2 - 60, 20))
    if state == "menu":
        screen.blit(small.render("SPACE = 2 players   1 = vs computer", True, (200, 200, 200)), (220, 300))
    elif state == "over":
        who = "Left" if scores[0] > scores[1] else "Right"
        screen.blit(small.render(f"{who} player wins! SPACE to play again", True, (255, 200, 0)), (210, 300))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
