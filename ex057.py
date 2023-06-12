'''Exercício Python 057: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
 Caso esteja errado, peça a digitação novamente até ter um valor correto'''
verificação = 0
while verificação == 0:

    sexo = str(input('Informe seu sexo : [M/F]')).strip().lower()[0]
    if sexo != 'f' and sexo != 'm':
        print('Dados invalidos.')
    else:
        verificação = 1

print('Sexo {} registrado com sucesso'.format(sexo).upper())