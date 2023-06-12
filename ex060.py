import math

y = int(input('Digite um numero \nPara calcular o fatorial: '))
x= math.factorial(y)
c = y
f =1
print(f'Calculando {y}! =', end= '')
while c > 0:
    print(f' {c} ', end='')
    print('x' if c> 1 else '=', end= '')
    f *= c                                     # fatorial matematicamente.
    c -= 1


print(f'  {f}')


