frase = str(input('digite uma frase: ')).lower().strip()


print('A letra A aparece {} vezes na frase'.format(frase.count('a')))
print('A primeira aparicao da letra A foi na posicao {}'.format(frase.find('a')+1))
print('A ultima aparicao da letra A foi na posicao {}'.format(frase.rfind('a')+1))