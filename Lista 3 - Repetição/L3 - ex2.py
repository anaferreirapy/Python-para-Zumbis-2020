#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao
#nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = str(input('Informe um nome para o usuário:'))
senha = str(input('Informe uma senha:'))

while (senha == nome):
    print('Senha inválida! Informe os dados novamente.')
    nome = str(input('Informe um nome para o usuário:'))
    senha = str(input('Informe uma senha:'))
