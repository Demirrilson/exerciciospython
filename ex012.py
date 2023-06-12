print('Dar um desconto de 5% em um produto')

valor_sem_desc = float(input('Qual o valor do Produto? R$'))

valor_com_desc = valor_sem_desc * 0.95

print('O valor do produto é de R${:.2f}\n O valor do produto com um desconto de 5% é de R${:.2f}' .format(valor_sem_desc, valor_com_desc))
print('\n\nO desconto foi de R${:.2f}' .format(valor_sem_desc * 0.05))
