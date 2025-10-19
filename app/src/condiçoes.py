tempo = int(input('quantos anos tem seu carro? '))

#if tempo <=3:
#    print('Seu carro eh novo!')
#else:
#    print('Seu carro eh velho!')
'conseguimos simplicifar a condicao em apenas uma linha:'
print('carro novo' if tempo <=3 else 'carro velho')

print('FIM!')