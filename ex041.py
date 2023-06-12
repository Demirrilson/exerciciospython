#Exercício Python 041: A Confederação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#- Até 9 anos: MIRIM
#- Até 14 anos: INFANTIL
#- Até 19 anos: JÚNIOR
#- Até 25 anos: SÊNIOR
#- Acima de 25 anos: MASTER
from datetime import date

nasc = int(input('Qual o ano de nascimento do Atleta? '))

idade = date.today().year - nasc
print('O atleta de nasceu em {} tem {} anos'.format(nasc, idade))
if idade < 9 :
    print('A categoria é MIRIM')
elif 9 <= idade < 14:
    print('A categoria é INFANTIL')
elif 14 <= idade < 19:
    print('A categoria é JUNIOR')
elif 19 <= idade < 25:
    print('A categoria é SENIOR')
else:
    print('A categoria é MASTER')
