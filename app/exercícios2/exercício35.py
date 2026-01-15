casa = float(input('informe o valor da casa: R$'))
salario = float(input('informe seu rendimento salarial: R$'))
anos = int(input('Em quantos anos deseja pagar? '))
prestação = casa / (anos * 12)

if (prestação<=salario*0.3):
    print('seu emprestimo foi APROVADO, o valor das prestações ficará em R${:.2f}'.format(prestação))
else:
    print('seu emprestimo foi NEGADO, pois o valor das prestações ficará em R${:.2f}'.format(prestação))