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
