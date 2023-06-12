print('fazer um programa que calcula a area da parede e o rendimendo da tinta\n')

comprimento = float(input('Qual o comprimento da parede em metros: '))
altura = float(input('Qual a alturaa da parede em metros: '))
rendimento = float(input('Qual o rendimento da tinta em L/M²: '))

area = comprimento * altura
cobertura = area / rendimento

print('\n\nA parede tem {}x{}M, sua area é de {:.2f}M², \npara pintar precisa de {:.2f}L de tinta' .format(comprimento, altura, area, cobertura))