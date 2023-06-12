#Exercício Python 042: Refaça o DESAFIO 035 dos triângulos,
# acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferente

print('Os segmentos formam um triangulo?')
a = float(input('Digite o 1º segmento: '))
b = float(input('Digite o 2º segmento: '))
c = float(input('Digite o 3} segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('Os segmentos formam um ',end='')
    if a==b and a==c:
        print('TRIANGULO EQUILÁTERO')
    elif a!=b and a!=c:
        print('TRIANGULO ESCALENO')
    else:
        print('TRIANGULO ISÓSCELES')
else:
    print('Os segmentos NÂO formam um triangulo')