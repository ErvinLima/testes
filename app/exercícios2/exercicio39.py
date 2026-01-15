n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

Media = (n1+n2)/2
print('Tirando {} e {}, a media do aluno eh {}'.format(n1,n2,Media))

if Media >= 7:
    print('O aluno esta APROVADO')
elif Media > 5:
    print('O aluno esta REPROVADO')
elif 7 > Media >= 5 :
    print('O aluno esta de RECUPERACAO')