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
