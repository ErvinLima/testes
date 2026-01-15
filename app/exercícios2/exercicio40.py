from datetime import date

nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade = atual - nasc
print('O atleta tem {} anos.'.format(idade))

if idade <= 9:
    print('Classificacao: Junior')
elif idade <= 14:
    print('Classificacao: INFANTIL')
elif idade <= 19:
    print('Classificacao: JUNIOR')
elif idade <= 25:
    print('Categoria: SENIOR')
else: 
    print('Categoria: MASTER')