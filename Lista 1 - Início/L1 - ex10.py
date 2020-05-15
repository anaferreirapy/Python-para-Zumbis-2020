#Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a
#quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante
#perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o
#total de dias.

qtcig = int(input('Informe a quantidade de cigarros que você fuma por dia:'))
anos = int(input('Informe por quantos anos você já fumou/fuma:'))

r = (qtcig * anos * 365) / 144

print(f'Você perdeu {r: .1f} dias da sua vida por fumar.')


