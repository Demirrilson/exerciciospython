#Exercício Python 036: Escreva um programa para aprovar o empréstimo bancário para
# a compra de uma casa. Pergunte o valor da casa, o salário do comprador e
# em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[1;32mAnalise de perfil para emprestimo imobiliario\033[m')
#nome = str(input('Digite seu nome: '))
vcasa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o seu salario? R$'))
tempo = int(input('Em quantos anos pretende pagar? '))

parcela = vcasa/(tempo*12)
por = (parcela*100)/salario

if parcela <= (0.3*salario):
    print('PARABENS! \nSeu emprestimo foi aceito. A parcela ficou \033[1;42mR${:.2f}\033[m' .format(parcela))
    print('Este valor equivale \033[1;32m{:.1f}%\033[m do seu salario' .format(por))
else:
    print('O emprestimo não foi aprovado, devido a parcela de \033[1;41mR${:.2f},\033[m corresponder a \033[1;41m{:.1f}% \033[mdo seu salario'.format(parcela, por))
