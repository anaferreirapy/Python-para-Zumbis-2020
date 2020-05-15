#Imprima os números pares de 0 até o número lido.

n = int(input('Informe um número qualquer:'))

x = 0

while x <= n:
    x = x + 1
    if x%2 == 0:
        print (x)
