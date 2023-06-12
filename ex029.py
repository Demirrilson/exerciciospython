#Exercício Python 029: Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite
vel = int(input('\nQual a sua velocidade? '))
multa = float((vel-80)*7.00)
if vel> 80:
    print('MULTADO! você exedeu o limite de 80 KM/h')
    print('Você de pagar um valor R$ {:.2f} '.format(multa))
print('Dirija com cuidado!')