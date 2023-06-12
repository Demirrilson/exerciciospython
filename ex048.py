#Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um
# número que o usuário escolher, só que agora utilizando um laço for

numero = int(input('Digite um numero para saber sua tabuada: '))

for x in range (0,11):
    print('{} X {} = {}' .format(numero, x, numero*x))