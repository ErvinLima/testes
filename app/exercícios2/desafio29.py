num = int(input('informe qualquer numero: '))
div = num % 2

if div == 0:
    print('O numero {} eh par'.format(num))
else:
    print('O numero {} eh impar'.format(num))