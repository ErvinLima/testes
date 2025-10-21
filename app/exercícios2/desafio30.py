km = float(input('qual a distancia da viagem em km? '))

if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('Com a distancia de {}km o valor da passagem fica em R${:.2f}'.format(km, preço))
