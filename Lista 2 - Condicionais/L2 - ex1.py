#Faça um Programa que peça os três lados de um triângulo. O programa deverá informar se os valores podem ser
#um triângulo. Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.

#Equilatero: todos os lados iguais.
#Isosceles: Dois lados iguais.
#Escaleno: Todos os lados diferentes.

a = float(input('Informe a medida do primeiro lado do triângulo:'))
b = float(input('Informe a medida do segundo lado do triângulo:'))
c = float(input('Informe a medida do terceiro lado do triângulo:'))

if a > b + c or b > a + c or c > a + b:
    print('Não pode ser um triângulo. Um dos lados é maior que a soma dos outros dois.')
elif a == b == c:
    print('Triângulo Equilátero')
elif a == b or b == c or a == c:
    print('Triangulo Isósceles')
else:
    print('Triângulo Escaleno')
