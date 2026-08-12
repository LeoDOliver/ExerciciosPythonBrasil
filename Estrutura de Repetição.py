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
  
