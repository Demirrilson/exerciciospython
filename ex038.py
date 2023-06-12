x=float(input('Digite o primeiro numero: '))
y=float(input('Digite o segundo numero: '))

if x<y:
    print('O maior numero é o segundo {} e o menor é o primeiro {} '.format(y,x))
elif x>y:
    print('O maior é o primeiro {} e o menor é o segundo {}' .format(x,y))
else:
    print('O primeiro e segundo numero são iguais: {} '.format(x))
