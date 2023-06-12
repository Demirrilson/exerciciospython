#Exercício Python 039: Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import  date

nascimento = int(input('Qual ano você nasceu? '))
ano = date.today().year
idade = ano - nascimento

if idade<18:
    print('Você tem {} anos e ainda faltam {} anos para seu ALISTAMENTO' .format(idade, 18-idade))
elif idade > 18:
    print('Você tem {} anos e ja passaram {} anos do seu ALISTAMENTO' .format(idade,  idade-18))
else:
    print('Você tem {} e esta no tempo de se ALISTAR.' .format(idade))