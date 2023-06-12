lista = (
'Lapis', 1.75, 'Borracha', 2.00, 'caderno', 15.90, 'Estojo', 25.00, 'transferidor', 4.20, 'compasso', 9.99, 'mochila',
120.32, 'canetas', 22.30, 'livro', 34.90)
c_impar = (-1)
c_par = (-2)
print('-=' * 20)
print('{:^40}'.format('LISTA PYTHON'))
print('-=' * 20)
for x in range(0, len(lista) // 2):
    c_impar += 2
    c_par += 2
    print(' ', '{:.<26} R${:>7} '.format(lista[c_par], lista[c_impar]))
print('-=' * 20)

