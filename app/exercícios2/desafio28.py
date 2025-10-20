velo = float(input('Qual a velocidade do seu carro? '))

if velo > 80:
    print('Mutado! Você excedeu o limite de velocidade permitido que é de 80KM/h' )
    multa = (velo - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))

print('Tenha um bom dia! Dirija com seguranca!')