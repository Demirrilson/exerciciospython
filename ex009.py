print('\nDigite um numero e obtenha sua tabuada\n')

x = int(input('Digite um valor: '))
count = 0
while count<=10:
    z=x*count
    print('{}x{}={}'.format(x, count, z))
    count+=1