"""Exercício 01
Faça um programa para imprimir:

1
2   2
3   3   3
.....
n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha."""

def impressaon(n):
  for i in range(1,n+1):
    aux = str(i) + " "
    print(aux * i)

n = int(input("Digite n: "))
impressaon(n)

"""Exercício 02
Faça um programa para imprimir:

1
1   2
1   2   3
.....
1   2   3   ...  n
Para um n informado pelo usuário. Use uma função que receba um valor n inteiro, imprima até a n-ésima linha."""

def impressao2(n):
  for i in range(1, n+1):
    if i == 1:
      print(1)
    else:
      for j in range(1,i+1):
        aux = str(j) + ""
      print(aux)

n = int(input("Digite n: "))
impressao2(n)
#Corrigir impressão


"""Exercício 03
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos."""

def soma(n1,n2,n3):
  soma = n1 + n2 + n3
  return soma

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

resultado = soma(n1,n2,n3)
print(resultado)
