n = input('Digite algo: ')

print(f'O tipo primitivo desse valor é <{type(n)}>')
print(f'Só tem espaços? {n.isspace()}')
print(f'É um numero? {n.isnumeric()}')
print(f'É alfabetico? {n.isalpha()}')
print(f'É alfanumero? {n.isalnum()}')
print(f'Esta em maiusculas? {n.isupper()}')
print(f'Esta em minusculas? {n.islower()}')
print(f'Esta capitalizada? {n.istitle()}')