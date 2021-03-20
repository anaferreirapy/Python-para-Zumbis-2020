#Faça um programa que receba um dado dd/mm/aaaa e escreva o mês por extenso.

mes = '''janeiro fevereiro março abril maio junho julho agosto setembro outubro novembro dezembro'''.split()

d,m,a = input('dd/mm/aaaa:').split('/')

print(f'{d} de {mes[int(m)-1]} de {a}')
