
print('Analizando nomes\n')

n = str(input('Digite seu nome completo: ')).strip()
n2 = n.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é: {}' .format(n2[0]))
print('Seu ultimo nome é: {}' .format(n2[-1]))