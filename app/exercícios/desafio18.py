import math
ang = float(input('informe o angulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tg = math.tan(math.radians(ang))

print('o seno do angulo de {} eh {:.2f}'.format(ang, sen))
print('o cosseno do angulo de {} eh {:.2f}'.format(ang, cos))
print('a tangente do angulo de {} eh {:.2f}'.format(ang, tg))