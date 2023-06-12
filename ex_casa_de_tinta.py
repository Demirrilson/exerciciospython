'''Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros,
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.'''
# 3.6l * 4 = R$100 =  14,4l
# 3.6l * 3 = R$75 = 10,8l

from math import ceil
print('-=-' * 21)
print('{:^62}'.format('LOJA DE TINTAS'))
print('-=-' * 21)
h = float(input('Digite a altura da parede:{:->27} '.format('')))
c = float(input('Digite o comprimento da parede:{:->22} '.format('')))
print('---' * 21)
area = h * c
rendimento = ceil((area / 6) * 0.9)
lata_preco = 80
galao_preco = 25
lata_v = 18
galao_v = 3.6
galoes = 0
quantidade = 0
sobra = 0
latas = rendimento // lata_v
sobra = rendimento % lata_v
quantidade = lata_v * latas
if sobra > 10.8:
    latas += 1
    quantidade = lata_v * latas
elif sobra < 10.8 and sobra > 0:
    galoes = ceil(sobra / galao_v)
    quantidade = quantidade + (galao_v * galoes)
print('Area de parede a ser pintada {:.>24} {:.2f}M²'.format('', area))
print('Quantidade de tinta necessaria para pintura: {:.>8} {}L'.format('', rendimento))
print('---' * 21)
print('Quantidade de latas de tinta de 18L:{:.>17} {} '.format('', latas))
print('Quantidade de galões de tinta de 3.6L:{:.>15} {} '.format('', galoes))
print('Quantidade de tinta comprada {:.>24} {}L'.format('', quantidade))
print('---' * 21)
print('Valor gasto em latas {:.>32} R${:.2f}'.format('', latas * lata_preco))
print('Valor gasto em galões{:.>32} R${:.2f}'.format('', galoes * galao_preco))
print('Valor Total gasto em tinta {:.>26} R${:.2f}'.format('', galoes * galao_preco + latas * lata_preco))
print('---' * 21)
print('Sobra de tinta {:.2f}L'.format(quantidade - rendimento))

# print('\n{}'.format(sobra))