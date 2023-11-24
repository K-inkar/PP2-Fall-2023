import pygame
import os

pygame.init()

pygame.display.set_mode((100, 100))

music_files = ['start.mp3', 'stop.mp3', 'next.mp3', 'previous.mp3']

music_index = 0

def play_music():
    pygame.mixer.music.load(music_files[music_index])
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def next_song():
    global music_index
    music_index = (music_index + 1) % len(music_files)
    play_music()

def previous_song():
    global music_index
    music_index = (music_index - 1) % len(music_files)
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:  # Клавиша 's' для воспроизведения
                play_music()
            elif event.key == pygame.K_w:  # Клавиша 'w' для остановки
                stop_music()
            elif event.key == pygame.K_d:  # Клавиша 'd' для следующей песни
                next_song()
            elif event.key == pygame.K_a:  # Клавиша 'a' для предыдущей песни
                previous_song()

pygame.quit()
