s1 = float(input('informe o primeiro segmento: '))
s2 = float(input('informe o segundo segmento: '))
s3 = float(input('informe o terceiro segmento: '))

if s1< s2+s3 and s2<s1+s3 and s3<s1+s2:
    print('Os segmentos podem formar um triangulo')
else:
    print('Os segmentos nao podem formar um triangulo')