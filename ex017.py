print('calcular hip de um triangulo retangulo\n')

import  math

ca = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))

#hip = math.sqrt((math.pow(ca,2) )+ (math.pow(co,2)))
hip = math.hypot(ca, co)
print('\nA hipotenusa é {:.2f}'.format(hip))