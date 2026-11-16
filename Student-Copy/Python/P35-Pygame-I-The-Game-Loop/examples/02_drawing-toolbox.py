RED = (220, 50, 50)
pygame.draw.rect(screen, RED, (50, 50, 100, 60))
pygame.draw.rect(screen, RED, (200, 50, 100, 60), 3)  # outline
pygame.draw.circle(screen, (0, 200, 255), (400, 80), 30)
pygame.draw.line(screen, (255, 255, 255), (0, 300), (800, 300), 2)
pygame.draw.polygon(screen, (0, 255, 100),
                    [(600, 50), (650, 150), (550, 150)])

font = pygame.font.SysFont("arial", 36)
text = font.render("Score: 10", True, (255, 255, 255))
screen.blit(text, (20, 540))
