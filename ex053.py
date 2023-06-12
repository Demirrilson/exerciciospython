#Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = str(input('Digite uma frase: ')).lower().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso +=junto[letra]

print('O inverso de {} é {}'.format(junto , inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('Não é um palindromo')
