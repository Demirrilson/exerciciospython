lista = []
teste = ''
contem = 0
lista.append(int(input('Digite um valor: ')))
while True:
    teste = str(input('Deseja continuar? [S/N]')).upper()[0]
    if teste == 'N':
        break
    elif teste != 'S':
        teste = str(input('Deseja continuar? [S/N]')).upper()[0]
    else:
        lista.append(int(input('Digite um valor: ')))
for num in lista:
    if num == 5:
        contem = 1
print('A lista em ordem decrescente é: {}'.format(sorted(lista, reverse=True)))
print('A quantidade de elementos na lista é: {}'.format(len(lista)))
if contem == 1:
    print('Contém o numero 5 na lista')
else:
    print('Não contém o numero 5 na lista')

