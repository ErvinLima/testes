num = int(input('informe um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {}'.format(u))
print('dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))