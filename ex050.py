#Exercício Python 050: Desenvolva um programa que leia seis números inteiros e
# mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o
soma = 0
count = 0
for c in range (0,6):

    itens= int(input('Digite o {}° valor :'.format(c+1)))
    if itens % 2 == 0:
        soma = soma + itens
        count += 1
print(' Você digitou {} numeros PARES e a soma é {}'.format(count, soma))
