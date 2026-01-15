res = str(input('Voce deseja comparar dois numero e saber quem e maior entre eles?').upper())
if res == 'SIM':
    num1 = int(input('Informe o primeiro numero: '))
    num2 = int(input('informe o segundo numero: '))

    if num1>num2:
        print('o numero {} eh maior do que o numero {}.'.format(num1, num2))
    elif num2>num1: 
        print('o numero {} eh maior do que o numero {}'.format(num2, num1))
    elif num1==num2:
        print('Os numeros sao iguais!')
    else:
        print('nao consegui identificar os numeros')

elif res == 'NÃO' or res == 'NAO':
    print('Entendi, volte sempre!')
else:
    print('Nao entendi, tente novamente!')