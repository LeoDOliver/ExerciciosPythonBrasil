"""Exercício 01
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e 
são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente."""


texto1 = input("Digite a primeira string: ")
texto2 = input("Digite a segunda string: ")

if len(texto1) == len(texto2):
  print("Comprimento igual")
else:
  print("Comprimento diferente)

if (texto1.upper()) == (texto2.upper()):
   print("Conteúdo igual)
else:
   print("Conteúdo diferente")

"""Exercício 02
Nome ao contrário em maiúsculas. 
Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. 
Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas."""

nome = input("Digite um nome: ")
nome = nome[::-1]
nome = nome.upper()
print(nome)
