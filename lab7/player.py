import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Music Player")

WHITE = (255, 255, 255)
GRAY = (220, 220, 220)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)

font = pygame.font.SysFont("Arial", 28, bold=True)

playlist = [
    "songs/Chronos.mp3",
    "songs/house_lo.mp3",
    "songs/Overdrive-Matrika.mp3"
]

current_song_index = 0

def draw_button(x, y, w, h, text):
    pygame.draw.rect(screen, GRAY, (x, y, w, h), border_radius=10)
    pygame.draw.rect(screen, BLACK, (x, y, w, h), 2, border_radius=10)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect(center=(x + w // 2, y + h // 2))
    screen.blit(text_surface, text_rect)

def load_and_play(index):
    pygame.mixer.music.load(playlist[index])
    pygame.mixer.music.play()
    print(f"Playing: {playlist[index]}")

load_and_play(current_song_index)

clock = pygame.time.Clock()

button_width, button_height = 100, 50
buttons = {
    "Play": (50, 300),
    "Stop": (170, 300),
    "Prev": (290, 300),
    "Next": (410, 300)
}

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.mixer.music.stop()
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for name, (bx, by) in buttons.items():
                if bx <= mx <= bx + button_width and by <= my <= by + button_height:
                    if name == "Play":
                        load_and_play(current_song_index)

                    elif name == "Stop":
                        pygame.mixer.music.stop()
                        print("Stopped")

                    elif name == "Next":
                        current_song_index = (current_song_index + 1) % len(playlist)
                        load_and_play(current_song_index)

                    elif name == "Prev":
                        current_song_index = (current_song_index - 1) % len(playlist)
                        load_and_play(current_song_index)

    song_name = os.path.basename(playlist[current_song_index])
    title_surface = font.render(f"Now Playing: {song_name}", True, BLACK)
    title_rect = title_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(title_surface, title_rect)

    for name, (x, y) in buttons.items():
        draw_button(x, y, button_width, button_height, name)

    pygame.display.flip()
    clock.tick(30)
