#Exercício Python 051: Desenvolva um programa que leia o primeiro termo
# e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('Calculo de P.A.')

primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razâo: '))
termos = int(input('Digite a quantidade de termos: '))
an = 0
for c in range (0, termos):
    an = primeiro_termo + c * razao
    print(an, end=' → ')
print('Acabou')
