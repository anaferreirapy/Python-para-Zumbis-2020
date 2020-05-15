#Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo
#usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar,
#sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Informe a quantidade de kms percorridos com o veículo:'))
dias = int(input('Informe a quantidade de dias de aluguel do veículo:'))

preço = dias * 60 + km * 0.15

print('O valor a se pagar é: R$ ',preço)

