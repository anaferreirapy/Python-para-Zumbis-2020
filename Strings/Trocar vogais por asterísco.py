#Faça um programa que troque as vogais de uma palavra por "*".

palavra = input('Palavra: ')
k = 0
troca = ''
while k < len(palavra):
    if palavra[k] in 'aeiou':
        troca = troca + '*'
    else:
        troca = troca + palavra[k]
    k = k + 1
print(troca)
