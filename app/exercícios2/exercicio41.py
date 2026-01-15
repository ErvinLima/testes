s1 = float(input('Primeiro seguimento: '))
s2 = float(input('Segundo seguimento: '))
s3 = float(input('Terceiro seguimento: '))

if s1< s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('Os segmentos podem formar um triangulo', end=' ')
    if s1 == s2 == s3:
        print('equilatero! ')
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print('isosceles')
    elif s1 != s2 != s3 != s1:
        print('escaleno')
else:
    print('os seguimentos nao podem formar um triangulo')