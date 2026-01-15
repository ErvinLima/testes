from datetime import date

atual = date.today().year
ano = int(input('informe o seu ano de nascimento: '))
idade = atual - ano
alistamento = ano + 18

print('Quem nasceu em {} tem {} anos em {}'.format(ano, idade, atual))

if idade < 18:
    print('Seu ano de alistamento eh em {}'.format(alistamento))
elif idade > 18:
    print('Voce deveria ter se alistado ha {} anos'.format(atual - (alistamento)))
    print('Seu alistamento foi em {}'.format(alistamento))
elif idade == 18:
    print('Esta eh a hora exata de se alistar!')