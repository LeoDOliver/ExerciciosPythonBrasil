#01 - Faça um programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
  print(f"{num1} é maior do que {num2}")
elif num2 > num1:
  print("{num2} é maior do que {num1}")
else:
  print("Os números digitados são iguais")




#02 - Faça um programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = int(input("Digite o número: "))

if num < 0:
    print("Número negativo")
elif num > 0:
    print("Número positivo")
else:
    print("O número digitado é 0, ou seja, nulo.")

#03 - Exercício 03

#Faça um programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:

#    F - Feminino
#    M - Masculino
#    Sexo Inválido.

sexo = input("Digite o sexo:")

if sexo.upper() == "F":
  print("F - Feminino")
elif sexo.upper == "M":
  print("M - Masculino")
else:
  print("Sexo Inválido.")


#Exercício 04 - Faça um programa que verifique se uma letra digitada é vogal ou consoante.

letra = input("Digite uma letra: ")

if letra.lower() in "aeiou":
  print("Vogal")
else:
  print("Consoante")




#Exercício 05 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

""" A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez."""

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2)/2

if media == 10:
  print("Aprovado com Distinção")
elif media > 7 and media < 10:
  print("Aprovado")
elif media < 7 and media > 0:
  print("Reprovado")
else:
  print("As notas informadas geraram um valor invalido.")



#Exercício 06 - Faça um programa que leia três números e mostre o maior deles:

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
  print(f"{num1} é o maior.")
elif num2 > num1 and num2 > num3:
  print(f"{num2} é o maior.")
elif num3 > num1 and num3 > num2:
  print(f"{num3} é o maior.")
else:
    if num1 == num2 and num1 > num3:
        print(f"Os dois primeiros números são iguais e maior que {num3}")
    elif num1 == num3 and num1 > num2:
        print(f"O primeiro e o terceiro número são iguais e maior que {num2}")
    elif num2 == num3 and num2 > num1:
        print(f"Os dois últimos números são iguais e maior que {num1}")
    else:
        print("Os números informados são iguais.")


#Exercício 07 - Faça um programa que leia três números e mostre o maior e o menor deles:

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))

if num1 > num2 and num1 > num3:
  print(f"{num1} é o maior")
  if num2 > num3:
    print(f"{num3} é o menor")
  else:
    print(f"{num2} é o menor")
elif num2 > num1 and num2 > num3:
  print(f"{num2} é o maior")
  if num1 > num3:
    print(f"{num3} é o menor")
  else:
    print(f"{num1} é o menor")
elif num3 > num1 and num3 > num2:
  print(f"{num3} é o maior")
  if num1 > num2:
    print(f"{num2} é o menor")
  else:
    print(f"{num1} é o menor")


#Exercício 08 - Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato:

prod1 = float(input("Digite o preço do primeiro produto: "))
prod2 = float(input("Digite o preço do segundo produto: "))
prod3 = float(input("Digite o preço do terceiro produto: "))

if prod1 == prod2 and prod1 == prod3:
  print("Os três produtos tem preços iguais"))
elif prod1 < prod2 and prod1 < prod3:
  print("O primeiro produto é o mais barato")
elif prod2 < prod1 and prod2 < prod3:
  print("O segundo produto é o mais barato")
elif prod3 < prod1 and prod3 < prod2:
  print("O terceiro produto é o mais barato")
else:
  if prod1 == prod2:
    if prod1 < prod3:
      print("O primeiro e o segundo produtos tem o mesmo preço e ambos são mais barato que o terceiro produto.")
    else:
      print("O terceiro produto é o mais barato")
  elif prod1 == prod3:
    if prod1 < prod2:
      print("O primeiro e o terceiro produtos tem o mesmo preço e ambos são mais barato que o segundo produto.")
    else:
      print("O segundo produto é o mais barato")
  else:
    if prod2 < prod1:
      print("O segundo e terceiro produto são mais baratos que o primeiro produto")
    else:
      print("O primeiro produto é mais barato")
    
#Exercício 09 -Faça um programa que leia três números e mostre-os em ordem decrescente:

"""Exercício 10

Faça um programa que pergunte em que turno você estuda. Peça para digitar:

    M - Matutino
    V - Vespertino
    N - Noturno.

Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turno = input("Em qual turno você estuda - \nM (Matutino)\nV (Vespertino)\nN (Noturno)\nDigite: ")

if turno.upper() == "M":
    print("Bom dia!")
elif turno.upper() == "V":
    print("Boa tarde!")
elif turno.upper() == "N":
    print("Boa noite!")
else:
    print("Valor Inválido!")

"""As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes. 
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:

    salários até R$ 280,00 (incluindo) : aumento de 20%
    salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    o salário antes do reajuste;
    o percentual de aumento aplicado;
    o valor do aumento;
    o novo salário, após o aumento.
"""
salario_atual = float(input("Digite seu salário atual: "))

if salario_atual <= 280 and salario_atual > 0:
    novo_salario = salario_atual + (salario_atual*20)/100
    print(f"Seu salário atual é R${salario_atual}, ele terá um reajuste de 20% ({(salario_atual*20)/100}) e seu novo salário passará a ser R${novo_salario}")
elif salario_atual > 280 and salario_atual <= 700:
    novo_salario = salario_atual + (salario_atual*15)/100
    print(f"Seu salário atual é R${salario_atual}, ele terá um reajuste de 15% ({(salario_atual*15)/100}) e seu novo salário passará a ser R${novo_salario}")
elif salario_atual > 700 and salario_atual <= 1500:
    novo_salario = salario_atual + (salario_atual*10)/100
    print(f"Seu salário atual é R${salario_atual}, ele terá um reajuste de 10% ({(salario_atual*10)/100}) e seu novo salário passará a ser R${novo_salario}")
elif salario_atual > 1500:
    novo_salario = salario_atual + (salario_atual*5)/100
    print(f"Seu salário atual é R${salario_atual}, ele terá um reajuste de 05% ({(salario_atual*5)/100}) e seu novo salário passará a ser R${novo_salario}")
else:
    print("Valor inválido")
