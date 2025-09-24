frase = 'o essencial é invisível aos olhos'

print(len(frase))
#indica o comprimento da frase 
print(frase.count('o')) 
#vai contar quantas vezes existe a letra dentro das aspas na frase indicada
print(frase.count('e',0))
#essa função vai fazer a contagem das letras com o fatiamento, começando pelo numero indicado e terminando um antes do segundo numero indicado
print(frase.find('é'))
#a função vai encontrar dentro da frase quantas vezes aparece o valor indicado dentro dos parenteses
print('essencial' in frase)
#essa função retorna se existe uma palavra chave dentro da frase 