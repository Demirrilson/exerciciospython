print('Calcular o valor do aluguel de um carro diaria R$60,00,  KM R$0,15.\n ')

d = float(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos KMs foram rodados? '))

valor = (d*60)+(km*0.15)

print('\nO valor do aluguel ficou R${:.2f} ' .format(valor))
