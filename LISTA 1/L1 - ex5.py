#Solicite o preço de uma mercadoria e o percentual de desconto. Exiba o valor do desconto e o
#preço a pagar.

mercadoria = float(input('Informe o valor da mercadoria:'))
desconto = float(input('Informe o percentual de desconto:'))

total = mercadoria - (desconto/100)*mercadoria
totaldesc = (desconto/100)*mercadoria

print('O valor total a pagar é R$: ',total,' e o valor de desconto aplicado é de R$: ',totaldesc)
