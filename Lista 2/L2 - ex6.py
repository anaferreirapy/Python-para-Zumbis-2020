#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule
#e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
#8% para o INSS e 5% para o sindicato, faça um programa que nos dê o salário bruto, quanto pagou ao INSS,
#quanto pagou ao sindicato e o salário líquido. Observe que Salário Bruto - Descontos = Salário Líquido. Calcule os
#descontos e o salário líquido, conforme a tabela abaixo:

#a. + Salário Bruto : R$
#b. - IR (11%) : R$
#c. - INSS (8%) : R$
#d. - Sindicato ( 5%) : R$
#e. = Salário Liquido : R$

vhora = float(input('Qual o valor que você ganha por hora trabalhada?:'))
qhoras = int(input('Quantas horas você trabalhou no mês?'))
bruto = qhoras * vhora

ir = bruto * 0.11
inss = bruto * 0.08
sind = bruto * 0.05
descontos = ir + inss + sind
liquido = bruto - descontos

print(f'Salário bruto: R$ {bruto: .2f}')
print(f'Imposto de Renda: R$ {ir: .2f}')
print(f'INSS:R$ {inss: .2f}')
print(f'Sindicato: R$ {sind: .2f}')
print(f'Salário Líquido: R$ {liquido: .2f}')
