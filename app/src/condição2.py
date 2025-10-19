n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a segunda nota: '))

m = (n1+n2)/2

print('a sua media foi tanta {:.1f}'.format(m))

if m >= 6.0:
    print('Voce passou de ano!')
else:
    print('Lamento, mas voce nao alcancou o rendimento!')

#Simplificando a condicao colocamos assim:
print('Parabens!' if m>=6.0 else 'Estude mais!')