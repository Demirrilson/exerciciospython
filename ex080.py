'''Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.'''
lista = []
for cont in range(0,5):
    valor = int(input('Digite um valor: '))
    if cont == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado no final da lista')
    else:
        posicao = 0
        while posicao <= len(lista):
            if valor <= lista[posicao]:
                lista.insert(posicao, valor)
                break

            posicao += 1
        print(f'O valor foi adicionado na posição {posicao}')

print(f'A lista ordenada é {lista}')

