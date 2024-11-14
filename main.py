import sys
import os
import pygame
from ctypes import cast, POINTER
from comtypes import CoInitialize, CoUninitialize
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

def play_sound(filename):
    pygame.mixer.init()
    try:
        pygame.mixer.music.load(filename)
        pygame.mixer.music.play(-1)  # Бесконечное воспроизведение
        while True:  # Бесконечный цикл
            pygame.time.Clock().tick(10)

    except pygame.error as e:
        print(f"Error playing sound: {e}")


if __name__ == "__main__":
    if hasattr(sys, '_MEIPASS'):
        filename = os.path.join(sys._MEIPASS, 'RickRoll.mp3')
    else:
        filename = "RickRoll.mp3"  # Путь к ресурсу при разработке

    play_sound(filename)
