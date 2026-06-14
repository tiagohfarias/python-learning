#Challange021 - MP3
import pygame
#inicializa o pygame e o mixer
pygame.init()
pygame.mixer.init()
#carrega a musica
pygame.mixer.music.load('jjkex021.mp3')
#define volume inicial
pygame.mixer.music.set_volume(0.1)
#começa a tocar
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    comando = input("Digite '+' para aumentar ou '-' para diminuir o volume: ")
    if comando == '+' :
        vol = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(min(vol + 0.1, 1.0))#adicionar 0.1 no volume atual, e 1.0 é o maximo de volume
        print(f'Volume atual: {pygame.mixer.music.get_volume():.1f}')
    elif comando == '-':
        vol = pygame.mixer.music.get_volume()
        pygame.mixer.music.set_volume(max(vol - 0.1, 0.0))#remover 0.1 no volume e o mínimo é 0.0
        print(f'Volume atual: {pygame.mixer.music.get_volume():.1f}')
    else:
        print('Comando não encontrado...')
    pygame.time.Clock().tick(10)