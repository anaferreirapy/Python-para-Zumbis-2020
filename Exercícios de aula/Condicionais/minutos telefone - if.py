#Considere a empresa de telefonia Tchau.
#ABaixo de 200 minutos, a empresa cobra R$ 0,20 por minuto.
#ENtre 200 e 400 minutos, o preço é de R$ 0,18.
#Acima de 400 minutos o preço por minuto é de R$ 0,15.
#Calcule sua conta de telefone.

min = int(input("Informe a quantidade de minutos consumidos:"))
if min < 200:
    v = min * 0.20
    print(f'O valor da sua conta é de: R$ {v: .2f}.')
if min >= 200 and min <=400:
    v = min * 0.18
    print(f'O valor da sua conta é de: R$ {v: .2f}.')
if min > 400:
    v = min * 0.15
    print(f'O valor da sua conta é de: R$ {v: .2f}.')
