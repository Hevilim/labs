
import pygame
from maps import *
from random import randrange


pygame.init()


def menu():
    WIDTH, HEIGHT = 800, 800
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Menu")

    running = True

    while running:

        screen.fill(pygame.Color("black"))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        print_text(screen, "Snake", WIDTH // 2 - 175, HEIGHT // 4, 125, "green")

        button(screen, WIDTH // 2 - 100, HEIGHT // 2 - 25, 200, 50, "grey", "white", "Play", "black", game)

        pygame.display.flip()


def game():

    RES = 800
    SIZE = 50

    screen = pygame.display.set_mode([RES, RES])
    pygame.display.set_caption("Snake")

    def generate_fruit():
        while True:
            apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            if (apple[0], apple[1]) not in lvl_map and (apple[1], apple[0]) not in snake:
                return apple[0], apple[1]

    def spawn():
        while True:
            x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
            if (x, y) not in lvl_map and (x,y):
                return x, y

    x, y = spawn()
    dirs = {"W": True, "S": True, "A": True, "D": True}
    snake = [(x, y)]
    apple = generate_fruit()
    dx, dy = 0, 0
    length = 1
    fps = 5

    clock = pygame.time.Clock()

    running = True

    while running:

        screen.fill("black")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                exit()

        key = pygame.key.get_pressed()

        if key[pygame.K_w] and dirs["W"]:
            dx, dy = 0, -1
            dirs = {"W": True, "S": False, "A": True, "D": True}
        if key[pygame.K_s] and dirs["S"]:
            dx, dy = 0, 1
            dirs = {"W": False, "S": True, "A": True, "D": True}
        if key[pygame.K_a] and dirs["A"]:
            dx, dy = -1, 0
            dirs = {"W": True, "S": True, "A": True, "D": False}
        if key[pygame.K_d] and dirs["D"]:
            dx, dy = 1, 0
            dirs = {"W": True, "S": True, "A": False, "D": True}

        [(pygame.draw.rect(screen, "green", (i + 1, j + 1, SIZE - 2, SIZE - 2))) for i, j in snake]
        pygame.draw.rect(screen, "red", (*apple, SIZE, SIZE))

        x += dx * SIZE
        y += dy * SIZE

        if y < 0:
            y = RES - SIZE
        elif y > (RES - SIZE):
            y = 0
        if x < 0:
            x = RES - SIZE
        elif x > (RES - SIZE):
            x = 0

        snake.append((x, y))
        snake = snake[-length:]

        if snake[-1] == apple:
            apple = generate_fruit()
            length += 1

        for i, j in lvl_map:
            pygame.draw.rect(screen, "grey", (i, j, SIZE, SIZE), 2)

        if len(snake) != len(set(snake)):
            running = False
            game_over(screen)

        for i, j in lvl_map:
            if i == x and j == y:
                game_over(screen)

        if key[pygame.K_ESCAPE]:
            pause(screen)

        pygame.display.flip()
        clock.tick(fps)


def game_over(surface):
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        print_text(surface, "Game Over", 50, 350, 50, "orange")

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            running = False
            menu()

        pygame.display.update()


def pause(surface):
    paused = True

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        print_text(surface, "Paused. Press enter to continue", 50, 100, 50, "orange")

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            paused = False

        pygame.display.update()


def print_text(surface, text, x, y, font_size, text_color):
    font = pygame.font.Font("font/arial.ttf", font_size)
    text_surface = font.render(text, True, text_color)
    surface.blit(text_surface, (x, y))


def button(surface, x, y, width, height, inactive_color, active_color, text, text_color, action):
    button_surface = pygame.Surface((width, height))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        button_surface.fill(active_color)
        if click[0] == 1:
            action()

    else:
        button_surface.fill(inactive_color)

    print_text(button_surface, text, 60, int(height * 0.075), int(height * 0.8), text_color)

    surface.blit(button_surface, (x, y)),


if __name__ == "__main__":
    menu()
