teste = ''
lista_geral = []
lista_par = []
lista_impar = []
lista_geral.append(int(input('Digite um valor: ')))
while True:
    teste = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if teste == 'N':
        break
    elif teste == 'S':
        lista_geral.append(int(input('Digite um valor: ')))
    else:
        teste = str(input('Deseja continuar? [S/N] ')).upper()[0]
for numero in lista_geral:
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)
print('Os valores digitados são: {}'.format(lista_geral))
print('Os valores IMPARES são: {}'.format(lista_impar))
print('Os valores PARES são: {}'.format(lista_par))
