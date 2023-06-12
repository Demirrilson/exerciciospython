'''Exercício Python 067: Faça um programa que mostre a tabuada de vários números,
 um de cada vez, para cada valor digitado pelo usuário.
 O programa será interrompido quando o número solicitado for negativo. '''

while True:
    print('--'*15)
    tab = int(input('Quer ver a tabuada de qual valor? '))
    if tab < 0:
        break

    for contador in range(1,11):
        print(f'{tab} x {contador} = {tab * contador}')
print('PROGRAMA ENCERRADO. VOLTE SEMPRE!')