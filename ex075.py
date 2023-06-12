nx = (int(input('Digite 1° valor: ')), int(input('digite 2° valor: ')), int(input('Digite 3° valor: ')),
      int(input('Digite 4° valor: ')))

print('Você digitou os valores {}'.format(nx))
print('O valor 9 apareceu {} vezes '.format(nx.count(9)))
if 3 in nx:
    print('O valor 3 aparece na {}° posição'.format(nx.index(3) + 1))
else:
    print('O valor 3 não digitado')
print('Os valores pares digitados foram: ', end='')
for count in nx:
    if count % 2 == 0:
        print(' {}'.format(count), end=' ')