print('tocar musica mp3\n')

import pygame
pygame.init()
pygame.mixer.music.load('ex0211.mp3')
pygame.mixer.music.play()
pygame.event.wait()
