#Digite um nome
#nome em maiusculas
#nome em minusculas
#quantidade de letras
#quantidade de letras do primero nome

nome = input('Digite seu nome: ')
print('Analisando seu nome...')
ma = nome.upper()
mi = nome.lower()
print('Seu nome em Maiúsculas é {}'.format(ma))
print('Seu nome em Minúsculas é {}'.format(mi))
esp=nome.count(' ')
n = len(nome)-esp
print('Seu nome tem ao todo {} letras' .format(n))
pn= nome.split()
nup  = len(pn[0])
print('Seu primeiro nome é {} e ele tem {} letras'.format(pn[0],nup))