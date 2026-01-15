nome = str(input('Qual o seu nome? '))
if nome == 'Ervin':
    print('Que nome diferente!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome e bem popular.')
else:
    print('Que nome legal!')
print('tenha um bom dia, {}!'.format(nome))