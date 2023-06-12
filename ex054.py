#Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
ano_atual = date.today().year
total_menor = 0
total_maior = 0
idade = 0
for c in range(1,8):
    ano = int(input('Em que ano nasceu a {}ª pessoa: ' .format(c)))
    idade = ano_atual - ano
    if idade >= 18:
        total_maior += 1
    else:
        total_menor += 1

print('\nExistem {} pessoas maiores de idade'. format(total_maior))
print(('\nExistem {} pessoas menores de idade' .format(total_menor)))