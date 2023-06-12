'''Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
 A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
mais_de_18 = homens = mulheres = contador = 0
teste = ''
print('Cadastro de Pessoas')
print('~~'*15)

while True:
    idade = int(input('Qual a idade? '))
    sexo = ''
    while sexo != 'f' and sexo != 'm':
        sexo =  str(input('Qual o sexo? [M/F] ')).strip().lower()[0]
    if idade > 18:
        mais_de_18 +=1
    if sexo == 'm':
        homens +=1
    if sexo == 'f':
        if idade < 20:
            mulheres +=1
    contador +=1
    teste = ''
    while teste != 'n' and teste != 's':
        teste = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
    if teste == 'n':
        break
print('~~'*15)
print(f'Foram entrevistadas {contador} pessoas.')
print(f'São {mais_de_18} pessoas com mais de 18 anos.')
print(f'Foram cadasrtrados {homens} homens.')
print(f'São {mulheres} mulheres com menos de 20 anos.')