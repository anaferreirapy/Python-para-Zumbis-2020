#Calcule o fatorial de um número lido.

n = int(input('Informe um número qualquer:'))

cont = 1

acm = 1

while cont <= n:
    acm = acm * cont
    cont = cont + 1

print (f'acm({n}) = {acm}')
