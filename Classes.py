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


bola1 = Bola("verde", 3.0, "Borracha")

bola1.mostra_cor()

nova_cor = input("Digite a nova cor: ")
bola1.troca_cor(nova_cor)
bola1.mostra_cor()

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


quadrado1 = Quadrado(5)
quadrado1.calcular_area()
quadrado1.retornar_lado()

novo_lado = int(input("Digite o novo valor do lado: "))
quadrado1.mudar_lado(novo_lado)
quadrado1.calcular_area()

"""Exercício 03 - Crie uma classe que modele um retângulo:

    Atributos: Lado_a, Lado_b (ou Comprimento e Largura, ou Base e Altura, a escolher)
    Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;

Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois, deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local."""

"""Exercício 04 - Crie uma classe que modele uma pessoa:

    Atributos: nome, idade, peso e altura
    Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.
"""

"""Exercício 05 - Crie uma classe para implementar uma conta corrente. 
A classe deve possuir os seguintes atributos: número da conta, nome do correntista e saldo. 
Os métodos são os seguintes: alterarNome, depósito e saque; No construtor, saldo é opcional, com valor default zero e os demais atributos são obrigatórios."""

class ContaBancaria:
    def __init__(self, n_conta, nome_correntista, saldo):
        self.n_conta = n_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def alterarNome(self):
        novo_nome = input("Digite o novo nome: ")
        self.nome_correntista = novo_nome

    def deposito(self):
        valor = float(input("Digite o valor a ser depositado: "))
        self.saldo += valor

    def saque(self):
        valor = float(input("Digite o valor a ser sacado: "))
        self.saldo -= valor


nome = input("Digite o seu nome: ")
n_conta = input("Digite o número da sua conta: ")
saldo = float(input("Digite o saldo da conta: "))

conta1 = ContaBancaria(n_conta, nome, saldo)

"""Exercício 06 - Faça um programa que simule um televisor criando-o como um objeto. 
O usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem dentro de faixas válidas."""

"""Exercício 07 - Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

    Atributos: Nome, Fome, Saúde e Idade b.
    Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade

Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação entre os atributos Fome e Saúde, ou seja, um campo calculado, 
então não devemos criar um atributo para armazenar esta informação por que ela pode ser calculada a qualquer momento. """


