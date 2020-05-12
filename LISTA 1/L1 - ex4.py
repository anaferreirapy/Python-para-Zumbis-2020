#Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a
#porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input('Informe o valor do salário:'))
reajuste = float(input('Informe o percentual de reajuste do salário:'))
novosalario = (reajuste/100)*salario+salario
print('O valor do novo salário é:',novosalario)
