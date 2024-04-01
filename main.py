import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGTH = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))

pygame.display.set_caption("ИГра ТИр")
icon = pygame.image.load("img/1612407962_17-p-tir-risunok-18.jpg")
pygame.display.set_icon(icon)

target_img = pygame.image.load("img/target_01.png")
target_width, target_height = 50, 50
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGTH - target_height)

color = random.randint(0, 155), random.randint(0, 155), random.randint(0, 155)

# Создаем пользовательское событие для перемещения мишени
MOVE_TARGET_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(MOVE_TARGET_EVENT, 1000)  # Таймер для перемещения мишени каждые 5 секунд

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == MOVE_TARGET_EVENT:
            # Перемещаем мишень
            target_x = random.randint(0, SCREEN_WIDTH - target_width)
            target_y = random.randint(0, SCREEN_HEIGTH - target_height)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if target_x < mouse_x < target_x + target_width and target_y < mouse_y < target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGTH - target_height)

    screen.blit(target_img, (target_x, target_y))
    pygame.display.update()

pygame.quit()
