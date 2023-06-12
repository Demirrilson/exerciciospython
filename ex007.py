print('LEr 2 notas e mostrar a media')

n1 = float(input('Digite a 1º nota: '))
n2 = float(input('Digite a 2º nota: '))
nc = float(input('Digite a nota de corte: '))

md = (n1+n2)/2

print('\nA media é {}' .format(md))

if md>=nc:
    print('\nAluno Aprovado')
else:
    print('Aluno Reprovado')
