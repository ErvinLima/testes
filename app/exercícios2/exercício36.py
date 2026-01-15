num = int(input('Escolha um numero inteiro e me informe: '))
print('''Escolha uma das bases para conversao:')
[1] converter para BINARIO')
[2] converter para OCTAL')
[3] converter para HEXADECIMAL''')
base = int(input('Qual base deseja utilizar? '))

if base == 1:
    print('O seu numero {} em binario fica {}'.format(num, bin(num)[2:])) #para removermos o comeco da identificacao do pyton para as formulas binarias e entre outras, usamos o metedo de fatiamento
elif base == 2:
    print('O seu numero {} em octal fica {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('O seu numero {} em hexadecimal fica {}'.format(num, hex(num)[2:]))
else:
    print('opcao invalida!')