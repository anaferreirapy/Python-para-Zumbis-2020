#Faça um Programa que leia três números e mostre o maior e o menor deles.

a = float(input('Informe o primeiro número:'))
b = float(input('Informe o segundo número:'))
c = float(input('Informe o terceiro número:'))

if a > b and a > c:
    print(f'Maior número é o: {a: .2f}')
elif b > a and b > c:
    print(f'Maior número é o: {b: .2f}')
else:
    print(f'Maior número é o: {c: .2f}')

if a <=b and a <= c:
    print(f'Menor número é o: {a: .2f}')
elif b <= c:
    print(f'Menor número é o: {b: .2f}')
else:
    print(f'Menor número é o: {c: .2f}')
