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

"""
Exercício 02 - Crie uma classe que modele um quadrado:

    Atributos: Tamanho do lado
    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
"""

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
        self.area = 0

    def mudar_lado(self, novo_lado):
        self.lado = novo_lado
        print("Lado alterado")

    def retornar_lado(self):
        print(f"O valor do lado do quadrado é {self.lado}")

    def calcular_area(self):
        self.area = (self.lado)**2
        print(f"A area do quadrado é {self.area}")


Quadrado1 = Quadrado(5)
Quadrado1.calcular_area()
Quadrado1.retornar_lado()

novo_lado = int(input("Digite o novo valor do lado: "))
Quadrado1.mudar_lado(novo_lado)
Quadrado1.calcular_area()
