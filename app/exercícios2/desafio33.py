salario = float(input('informe o salario para saber o aumento: '))

if salario >= 1250.0:
    aumento = salario + (salario * 10/100)
else:
    aumento = salario (salario * 15/100) 

print('Seu salario que era R${:.2f}, com aumento vai para {:.2f}'.format(salario, aumento))

