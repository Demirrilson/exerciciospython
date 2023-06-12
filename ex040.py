###Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
#- Média abaixo de 5.0: REPROVADO
#- Média entre 5.0 e 6.9: RECUPERAÇÃO
#- Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))

media = (n1 + n2)/ 2

if media < 5:
    print('O aluno esta REPROVADO sua media foi {}' .format(media))
elif media >=5 and media < 7:
    print('O aluno esta de RECUPERAÇÃO sua media foi {}'.format(media))
elif media>=7 and media < 10:
    print('O aluno esta APROVADO sua media foi {}'.format(media))
else:
    print('nota INVALIDA')