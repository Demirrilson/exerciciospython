lista = (
'programacao', 'das', 'coisas', 'chatas', 'e', 'quando', 'você', 'esta', 'na', 'casa', 'de', 'um', 'amigo', 'e', 've',
'que')

vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in lista:
    print('Na palavra {:^6} temos as vogais: '.format(palavra.upper()), end='')
    for letra in palavra:
        for vogal in vogais:
            if letra.count(vogal):
                print(' {}'.format(vogal.upper()), end='')
    print('\n')

