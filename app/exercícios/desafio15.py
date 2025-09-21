dis = float(input('informe a distancia percorrida pelo carro: '))
dias = int(input('informe a quantidade de dias alugados: '))

total = (dis * 0.15) + (dias *60)

print('o valor total a pagar do aluguel fica em R${}'.format(total))