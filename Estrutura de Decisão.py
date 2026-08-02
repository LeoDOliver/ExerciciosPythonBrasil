#01 - Faça um programa que peça dois números e imprima o maior deles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 > num2:
  print(num1, "é maior do que ", num2)
elif num2 > num1:
  print(num2, "é maior do que ", num1)
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

