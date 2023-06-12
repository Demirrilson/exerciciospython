print('\nA cidade que você nasceu começa com a palavra SANTO\n')
ci = (str(input('Qual cidade você nasceu? ')).strip()).lower()

print('santo' in ci[:6])
