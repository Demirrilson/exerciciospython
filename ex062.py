'''Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
 O programa encerrará quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA')
print('=-'*20)
p_termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))

contador = 0
termo = 0
teste = 10
total = 0
while teste != 0:
    while contador < teste:
        termo = p_termo + total * razao
        print(f'{termo} → ' , end='')
        contador +=1
        total += 1
    print('Pausa')
    teste = int(input('Quantos termos você quer mostrar a mais? '))
    if teste != 0:
        teste = contador + teste

print(f'PA finalizada com {total} termos mostrados')