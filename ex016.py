print('ler um numero real e mostrar sua porção inteira\n')

import math

num = float(input('Digite um valor '))

num_i = math.trunc(num)
print('A porção inteira de {} é {} '.format(num, num_i))
