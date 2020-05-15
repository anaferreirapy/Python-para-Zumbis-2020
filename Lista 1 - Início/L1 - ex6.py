#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média
#esperada para a viagem.

distancia = float(input('Informe a distância que será percorrida:'))
vmedia = float(input('Informe a velocidade média do percurso:'))

tempo = distancia/vmedia

print('O tempo da viagem de carro é: ',tempo,'h')
