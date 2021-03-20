#Faça um programa que informe se a palavra é palíndrome (escrita da mesma forma de tras para frente).

palavra = []

palavra = str(input('palavra: '))

if palavra == palavra[::-1]:
    print('A palavra é palíndrome')
else:
    print('A palavra não é palíndrome')
