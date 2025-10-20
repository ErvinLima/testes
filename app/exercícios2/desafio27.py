from random import randint
from time import sleep

num0 = randint(0, 5)
print('-=-'*20)
print('vou pensar em um numero entre 0 e 5. Tente adivinhar....')
print('-=-'*20)
jogador = int(input('Em qual numero eu pensei: '))
print('processando...')
sleep(3)

if jogador == num0:
    print('Parabens, voce acertou meu numero')
else:
    print('Errou, o numero que eu pensei foi o {}'.format(num0))