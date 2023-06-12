num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
       'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

valor = int(input('Digite um número de 0 a 20: '))

while True:

    while valor > 20:
        print('valor invalido')

        valor = int(input('Digite um número de 0 a 20: '))

    while valor < 0:
        print('valor invalido')

        valor = int(input('Digite um número de 0 a 20: '))

    if valor >= 0 and valor <= 20:
        print('Você digitou o número {}'.format(num[valor]))

        break