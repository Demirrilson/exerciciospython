from random import randint

x = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
maior = 0
menor = 0

print('Os valores sorteados foram:', end='')

for c in range(0, 5):
    y = x[c]
    print(' {}'.format(x[c]), end='')
    if c == 0:
        maior = y
        menor = y
    elif y > maior:
        maior = y
    elif y < menor:
        menor = y

print('\nO maior valor sorteado foi {}'.format(maior))
print('O menor valor sorteado foi {}'.format(menor))



