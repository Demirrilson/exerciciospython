# Informe um numero e mostre quantas unidades, dezenas, centanas e milhar

x = str(input('Digite um numero: ')).strip()
y = int(x)
print('Analisando o numero {}' .format(x))
print('Unidade = {}'.format(x[3:]))
print('Dezena = {}' .format(x[2:3]))
print('Centena = {}' .format(x[1:2]))
print('Milhar = {}' .format(x[:1]))
u = y // 1 % 10
d = y //10 % 10
c = y //100 % 10
m = y // 1000 %10

print('\nunidade {}\ndezena {}\ncentena {}\nmilhar {}' .format(u, d, c, m))


