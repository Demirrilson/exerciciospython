'''Exercício Python 083: Crie um programa onde o usuário
digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta.'''

expressao = str(input('Digite uma expresão: '))
verificacao = []
for elemento in expressao:
    if elemento == '(':
        verificacao.append(elemento)
    elif elemento == ')':
        if len(elemento) > 0:
            verificacao.pop()
        else:
            verificacao.append(elemento)
            break
if len(verificacao) == 0:
    print('A expreção é verdadeira.')
else:
    print('A expreção é falsa.')
