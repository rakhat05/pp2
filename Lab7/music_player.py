import pygame
import random

pygame.init()

def play_a_different_song():
    global currently_playing_song, songs
    next_song = random.choice(songs)
    while next_song == currently_playing_song:
        next_song = random.choice(songs)
    currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()

window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

song_end = pygame.USEREVENT + 1

songs = ['1.mp3', '2.mp3', '3.mp3']
currently_playing_song = None

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
                running = False
        if event.type == song_end:
            print("SONG ENDED!")
    window.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()

