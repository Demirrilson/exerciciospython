'''Exercício Python 061: Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.'''

print('Gerador de PA')
print('=-'*20)
p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

contador = 0
termo = 0

while contador < 10:
    termo = p_termo + contador * razao
    print(f'{termo} → ' , end='')
    contador +=1
print('FIM')