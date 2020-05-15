#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de
#seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do
#estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
#faça um programa que leia a variável peso (peso de peixes) e verifique se há excesso. Se houver, gravar na
#variável excesso e na variável multa o valor da multa que João deverá pagar. Caso contrário mostrar tais
# variáveis com o conteúdo ZERO.


kg = float(input('Informe a quantidade de kg de peixes:'))
           
if kg > 50:
    multa = (kg - 50) * 4
    excesso = kg - 50
    print('a quantidade de kg de peixes excedeu! A quantidade excedida é de: ',excesso,'kg.')
    print(f'E o valor total da  multa é de R$: {multa: .2f}')
else:
    print('Quantidade dentro do padrão!')
    multa = 0
    excesso = 0
    print('Excesso: ',excesso,' e Multa: ',multa,'.') 
