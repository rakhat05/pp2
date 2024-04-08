import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

BRUSH_SIZE = 10
ERASER_SIZE = 20

current_color = BLACK

def draw_rect(surface, color, start_pos, end_pos):
    pygame.draw.rect(surface, color, pygame.Rect(start_pos, (end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])))

def draw_circle(surface, color, center, radius):
    pygame.draw.circle(surface, color, center, radius)


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Простой Paint")


left_button_pressed = False
right_button_pressed = False
drawing_mode = "brush"  
start_pos = (0, 0)  
screen.fill(WHITE)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  
                left_button_pressed = True
                start_pos = event.pos
            elif event.button == 3:  
                right_button_pressed = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                left_button_pressed = False
            elif event.button == 3:
                right_button_pressed = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:  
                drawing_mode = "rect"
            elif event.key == pygame.K_c: 
                drawing_mode = "circle"
            elif event.key == pygame.K_e:  
                drawing_mode = "eraser"
            elif event.key == pygame.K_b:  
                drawing_mode = "brush"
            elif event.key == pygame.K_k:  
                current_color = BLACK
            elif event.key == pygame.K_w:  
                current_color = WHITE
            elif event.key == pygame.K_r: 
                current_color = RED
            elif event.key == pygame.K_g: 
                current_color = GREEN
            elif event.key == pygame.K_b:  
                current_color = BLUE

    if left_button_pressed or right_button_pressed:
        if drawing_mode == "brush":
            if left_button_pressed:
                pygame.draw.circle(screen, current_color, pygame.mouse.get_pos(), BRUSH_SIZE)
            elif right_button_pressed:
                pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), BRUSH_SIZE*5)
        elif drawing_mode == "rect":
            if left_button_pressed:
                draw_rect(screen, current_color, start_pos, pygame.mouse.get_pos())
        elif drawing_mode == "circle":
            if left_button_pressed:
                radius = ((pygame.mouse.get_pos()[0] - start_pos[0])**2 + (pygame.mouse.get_pos()[1] - start_pos[1])**2)**0.5
                draw_circle(screen, current_color, start_pos, int(radius))
        elif drawing_mode == "eraser":
            if left_button_pressed:
                pygame.draw.circle(screen, WHITE, pygame.mouse.get_pos(), ERASER_SIZE)

    pygame.display.flip()

pygame.quit()