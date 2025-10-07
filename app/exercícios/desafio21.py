nome = str(input('Digite seu nome completo: ')).strip()
div = nome.split()

print('O nome em Maiuscula {}'.format(nome.upper()))
print('O nome em minuscula {}'.format(nome.lower()))
print('O total de letras no seu nome é de {}'.format(len(nome) - nome.count(' '))) 

print('Seu primeiro nome tem {}'.format(len(div[0])))