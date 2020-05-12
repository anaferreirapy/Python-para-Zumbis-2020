#Sabendo que str( ) converte valores numéricos para string, calcule quantos dígitos há em 2 elevado
#a um milhão.

a = 2 ** 1000000

b = len(str(a))

print('2 elevado a 1000000, possui ',b,' dígitos.')
