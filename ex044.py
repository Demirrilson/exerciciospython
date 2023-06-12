#Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

compra = float(input('Qual o valor da compra? '))
print('FORMAS DE PAGAMENTOS:')
print('[1] à vista dinheiro / cheque \n[2] à vista no cartão \n[3] em até 2x no cartão \n[4] 3x ou mais no cartão')
opcao = int(input('Qual opção:'))
if opcao == 4:
    parcela = int(input('Em quantas vezes? '))
if opcao == 1:
    print('O valor a ser pago é R$ {:.2f} . Seu desconto foi de R${:.2f}'.format(compra*0.9, compra*0.1))
elif opcao ==2:
    print('O valor a ser pago é R${:.2f} . Seu desconto foi de R${:.2f}'.format(compra*0.95, compra*0.05))
elif opcao ==3:
    print('O valor da parcela é de R${:.2f}'.format(compra/2))
elif opcao==4:
    print('O valor total da compra foi de R${:.2f} o valor da parcela é de R${:.2f}'.format(compra*1.2, (compra*1.2)/parcela))
