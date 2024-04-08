import pygame
import sys
pygame.init()

w = 800
h = 600
l = pygame.display.set_mode((w,h))
pygame.display.set_caption("Moving Ball")

wc = (255, 255, 255)
rc = (255, 0, 0)

rad = 25
x = w // 2
y = h // 2
s = 20

clock = pygame.time.Clock()

Done = True
while Done:
    for event in  pygame.event.get():
        if event.type == pygame.QUIT:
            Done = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y = max(y - s, rad)
            elif event.key == pygame.K_DOWN:
                y = min(y + s, h - rad)
            elif event.key == pygame.K_LEFT:
                x = max(x - s, rad)
            elif event.key == pygame.K_RIGHT:
                x = min(x + s, w - rad)

    l.fill(wc)
    pygame.draw.circle(l, rc, (x, y), rad)
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
sys.exit()