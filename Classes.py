"""Exercício 01 - Crie uma classe que modele uma bola:

    Atributos: cor, circunferência, material
    Métodos: troca_cor e mostra_cor
"""

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, nova_cor):
        self.cor = nova_cor
        print("Cor alterada.")

    def mostra_cor(self):
        print(f"A cor da bola é {self.cor}")


Bola1 = Bola("verde", 3.0, "Borracha")

Bola1.mostra_cor()

nova_cor = input("Digite a nova cor: ")
Bola1.troca_cor(nova_cor)
Bola1.mostra_cor()
