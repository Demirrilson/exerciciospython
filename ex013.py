print('faça um algoritimo que calcule um aumento salarial\n')
salario = float(input('Qual o salario? R$'))
porc = float(input('Qual a % do aumento? '))

sal_novo = salario * ((porc/100)+1)

print('\nUm funcionario que ganhava R${:.2f}, com {}% de aumento, passa a receber R${:.2f}'.format(salario, porc, sal_novo))

print('\n O valor do aumento é de R${:.2f}' .format(salario * (porc/100)))
