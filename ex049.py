#Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são
# múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
elementos = 0
for x in range (1,501,2):
    if x % 3 == 0:
        soma = soma + x
        elementos = elementos + 1
print('A soma de todos os {} valores são {} '.format(elementos , soma))