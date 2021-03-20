#Ler 4 notas em uma lista e fazer a média delas.

nota = []
cont = 0
soma = 0

while (cont <=3):
    nota.append(float(input('Notas: ')))
    soma = soma + nota[cont]
    cont = cont + 1
print(f'Média: {soma/4: .1f}')

