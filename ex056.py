#Exercício Python 056: Desenvolva um programa que leia o nome,
# idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

media_idade = 0
mulheres = 0
nome_homem = ''
idade_homem = 0

for c in range(1, 5):

    print('{}ª pessoa' .format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().lower()

    media_idade += idade

    if sexo == 'f':
        if idade < 20:
            mulheres += 1

    if sexo == 'm':
        if idade > idade_homem:
            idade_homem = idade
            nome_homem = nome

print('A media de idade do grupo é de {} anos'.format(media_idade/4))
print('O homem mais velho tem {} anos e se chama {}. ' .format(idade_homem, nome_homem))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(mulheres))
