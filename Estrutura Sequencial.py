#Faça um Programa que mostre a mensagem "Alo mundo" na tela.

"""
print("Alo Mundo")
"""

#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].

"""
n = int(input("Digite um número: "))
print("O número informado foi %d." %n )
"""

#Faça um Programa que peça dois números e imprima a soma.

"""
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
soma = n1 + n2
print("A soma dos números é igual a %i." %soma )
"""

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""
n1 = float(input("Digite a nota do 1ºbimestre: "))
n2 = float(input("Digite a nota do 2ºbimestre: "))
n3 = float(input("Digite a nota do 3ºbimestre: "))
n4 = float(input("Digite a nota do 4ºbimestre: "))
media = (n1 + n2 + n3 + n4)/4
print("A sua média bimestral foi %.1f" %media )
"""

#Faça um Programa que converta metros para centímetros.

"""
m = float(input("Digite o valor em metros: "))
cm = m*100
print("O valor em centímetros é igual a %.f cm" %cm)
"""

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

"""
r = float(input("Digite o raio do círculo: "))
A = 3.14 * (r**2)
print("A área do círculo é igual a %.2f" %A)
"""

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

"""
l = float(input("Digite o lado do quadrado: "))
A = l**2
print("O dobro da aŕea deste quadrado é igual a %.1f" %(2*A))
"""

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.

"""
ganho = float(input("Quanto você ganha por hora? "))
horas = float(input("Quantas horas você trabalhou esse mês? "))
st = ganho * horas
print("O seu salário total no mês foi R$ %.2f" %st)
"""

#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

"""
f = float(input("Digite a temperatura em graus Fahrenheit: "))
c = 5 * ((f-32)/9)
print("A temperatura informada em Fahrenheit equivale a %.2f graus Celsius." %c)
"""

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

"""
c = float(input("Digite a temperatura em Celsius: "))
f = (9/5 * c) + 32
print("A temperatura informada em Celsius equivale a %.2f graus Fahrenheit." %f)
"""

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

"""
n1 = int(input("Digite um número inteiro: "))
n2 = int(input("Digite outro número inteiro: "))
r = float(input("Digite outro número real: "))
print("O produto do dobro do primeiro com metade do segundo é igual a %i, a soma do triplo do primeiro com o terceiro é %.1f e o terceiro elevado ao cubo é %.2f" %(n1*n2, 3*n1 + r, r**3))
"""

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58

"""
h = float(input("Digite sua altura: "))
psi = (72.7 * h) - 58
print("O seu peso ideal de acordo com a altura informada é %.2f quilos." %psi)
"""

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

"""
h = float(input("Digite sua altura: "))
sexo = input("Digite o seu sexo: ")
if sexo == "m" or sexo == "M":
    psi = (72.7 * h) - 58
elif sexo == "f" or sexo == "F":
    psi = (62.1*h) - 44.7
else:
    print("SEXO INVALIDO.")
print("O seu peso ideal de acordo com a altura informada é %.2f quilos." %psi)
"""

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente.
#João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

"""
kg = float(input("Quantos quilos você pescou hoje? "))
exc = kg - 50
if exc < 0 or exc == 0:
    print("Você não precisará pagar multa.")
else:
    multa = exc * 4
    print("Você tem %.1f quilos de excesso e terá de pagar uma multa de R$ %.2f." %(exc, multa))
"""

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:

#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

#Obs.: Salário Bruto - Descontos = Salário Líquido.

#Precisa de melhorias
"""
ganho = float(input("Quanto você ganha por hora? "))
horas = float(input("Quantas horas você trabalhou no mês? "))
sb = ganho * horas
dsc = (0.11 * sb) + (0.08 * sb) + (0.05 * sb)
sl = sb - dsc
print("+ Salario Bruto: R$" ,sb, "- IR(11%): R$" ,(0.11* sb), "- INSS(8%): R$" ,(0.08*sb),"- Sindicato: R$" ,(0.05*sb),"= Salario Liquido: R$",sl, sep="\n")
"""