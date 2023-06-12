print('No seu nome tem a palavra Silva\n')

s = (str(input('Qual o seu nome completo: ')).strip()).lower()

print('Contem Silva no nome?',('silva' in s))
