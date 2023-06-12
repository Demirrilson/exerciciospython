#Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
#- IMC abaixo de 18,5: Abaixo do Peso
#- Entre 18,5 e 25: Peso Ideal
#- 25 até 30: Sobrepeso
#- 30 até 40: Obesidade
#- Acima de 40: Obesidade Mórbida
print('Calculo de IMC')
peso = float(input('Digite o seu peso (KG): '))
altura = float(input('Digite a sua altura (M): '))
imc = peso / altura**2
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Voce esta abaixo do peso, ATENÇÂO!')
elif imc>= 18.5 and imc < 25:
    print('Você esta no peso Ideal, PARABENS!')
elif imc >= 25 and imc < 30:
    print('Você esta com Sobrepeso, CUIDADO COM OS DOCES!')
elif imc >=30 and imc < 40:
    print('Você esta com Obesidade, ATENÇÃO!')
elif imc >= 40:
    print('Você esta com Obesidade Morbida, PROCURE AJUDA MEDICA!')
min_ideal = (altura**2) * 18.5
max_ideal = (altura**2) * 25
print('Seu peso ideal esta entre {:.2f}Kg e {:.2f}Kg'.format(min_ideal, max_ideal))