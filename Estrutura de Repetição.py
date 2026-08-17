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
        print("Credencais aceitas")
        break

"""Exercício 03 - Faça um programa que leia e valide as seguintes informações:

    Nome: maior que 3 caracteres;
    Idade: entre 0 e 150;
    Salário: maior que zero;
    Estado Civil: 's', 'c', 'v', 'd';
"""

nome = input("Digite o seu nome: ")
idade = int(input("Digite sua idade: "))
salario = float(input("Digite o seu salário: "))
estado_civil = input("Digite seu estado civil - s, c, v ou d:")

cont = True
while True:
    if len(nome) <= 3:
        cont = False
    
    if idade < 0 or idade > 150:
        cont = False
    
    if salario < 0:
        cont =  False

    if estado_civil not in 'scvd':
        cont =  False

    if cont == False:
        print("Informações invalidas, redigite!)
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite sua idade: "))
        salario = float(input("Digite o seu salário: "))
        estado_civil = input("Digite seu estado civil - s, c, v ou d:")
        continue
    else:
        break
