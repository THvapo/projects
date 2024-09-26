import random
import time
import pygame

class cor:
    VERMELHO = '\033[31m'
    VERDE = '\033[32m'
    AMARELO = '\033[33m'
    AZUL = '\033[34m'
    MAGENTA = '\033[35m'
    CIANO = '\033[36m'

print(cor.AMARELO + '-=-'*10)
print(cor.VERMELHO + 'FAÇA SUA APOSTA!!')
print(cor.AMARELO + '-=-'*10)
print(cor.AZUL + 'VAMOS LÁ!')
aposta = str(input(cor.AZUL + 'o que você vai apostar? ')).strip()
casa = str(input(cor.AZUL + 'você quer apostar {} no slot VERMELHO ou PRETO? ' .format(aposta))).lower().strip()

print(cor.VERMELHO + 'ROLETANDO...')
pygame.init()
pygame.mixer.music.load('roleta.mp3')
pygame.mixer.music.play()
try:
    while pygame.mixer.music.get_busy():
        time.sleep(1)
except KeyboardInterrupt:
    pygame.mixer.music.stop()

pv = ('preto', 'vermelho')
pv2 = str(random.choice(pv))
if casa == pv2:
    print(cor.VERDE + 'Parabéns, você ganhou!')
    print(cor.VERDE + 'Você ganhou 6969 fichas, gaste como quiser na secretaria!')
else:
    print(cor.MAGENTA + 'faça o L, você perdeu, cuzão')

print(cor.CIANO + 'a casa escolheu o slot {}' .format(pv2))
