'''Exercício Python 079: Crie um programa onde o usuário possa digitar
vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado. No final, serão exibidos todos os valores únicos digitados,
em ordem crescente. '''

lista = []
fim = ''
teste = 0

while True:
    lista.append(int(input('Digite um valor: ')))

    if len(lista) > 1:
        teste = lista[len(lista)-1]
        #for numero in lista:
        for c in range(1, len(lista)):
            x = c - 1
            if teste == lista[x]:
                print('Valor duplicado! Não vou adicionar...')
                lista.pop()
    else:
        print('Valor adicionado...')

    fim = str(input(('Você deseja continuar? [S/N] '))).strip().upper()[0]
    if fim == 'N':
        break

    elif fim != 'S':
        fim = str(input(('Você deseja continuar? [S/N] ')))

lista.sort()
print(f'Você digitou os valores{lista}')
