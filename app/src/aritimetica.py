n1 = int(input('digite um valor: '))
n2 = int(input('Digite outro valor: '))

s = n1+n2 
m = n1*n2
d = n1/n2
di = n1//n2 #divisao inteira
e = n1**n2 #exponenciacao 

print ('A soma dos valores eh igual a {}, a mutiplicao {} e a divisao {}'.format(s, m, d))
#para indicar a quantidade de casa decimais desejadas na divisão precisa colocar assim {:.3f} no format.
print ('A divisao inteira eh igual a {} e sua exponenciacao {}'.format(di, e))
