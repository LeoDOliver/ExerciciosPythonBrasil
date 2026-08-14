"""Exercício 1

Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""

nota = int(input("Digite um nota entre 0 e 10: "))
while True:
    if nota > 10 or nota < 0:
        nota = int(input("Digite um nota entre 0 e 10: "))
    else:
        break

print(f"Nota aceita: {nota}")
  

"""Exercício 2 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
"""

username = input("Digite o nome de usuário: ")
senha =  input("Digite a senha: ")

while True:
    if username == senha:
        print("Nome de usuário e senha não podem ser iguais!")
        username = input("Digite o nome de usuário: ")
        senha =  input("Digite a senha: ")
    else:
        break
