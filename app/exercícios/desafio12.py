p = float(input('informe o preco do produto: '))

desc = p * 0.05
final = p - desc

print(p)
print('o produto teve o desconto de {} e seu valor final ficou em {}'.format(desc, final))