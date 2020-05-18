#Fatorial de um número lido.

cont = 1
acmd = 1

n = int(input('Informe um número:'))

while cont <= n:
    acmd = acmd * cont
    cont = cont + 1
    print(f'O fatorial de ({n}) é: {acmd}')
    
