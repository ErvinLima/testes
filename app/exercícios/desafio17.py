import math

co = float(input('informe o cateto oposto: '))
ca = float(input('informe o cateto adjacente: '))

hi = math.hypot(co, ca) #na biblioteca do math tem o metodo de calculo da hipotenusa
print('o valor da hipotenusa e {:.2f}'.format(hi))