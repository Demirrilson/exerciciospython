print('Digite um angulo e obtenha sen, cos, tg\n')

import  math

an = float(input('Digite o angulo que deseja: '))

cos = math.cos(math.radians(an))

sen = math.sin(math.radians(an))

tg = math.tan(math.radians(an))

print('Seno de {}º = {:.2f}' .format(an, sen))
print('Cosseno de {}º = {:.2f} ' .format(an, cos))
print('Tangente de {}º = {:.2f}' .format(an, tg))
