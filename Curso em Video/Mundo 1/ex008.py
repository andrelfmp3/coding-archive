# Condições simples e compostas
import random

tempo = int(input('Quantos anos tem seu carro?\n'))
if tempo <= 3:
    print('carro é novo')
else:
    print('carro é velho')
print('--FIM--')

print('carro é novo (simplificado)') if tempo<=3 else print('carro é velho (simplificado)')

nome = str(input('Qual é seu nome?\n'))
if nome == 'André':
    print('Olá, André')
else:
    print('Olá.')

n1 = float(input('Nota 1: \n'))
n2 = float(input('Nota 2: \n'))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'. format(m))

if m >= 6.0:
    print('Acima da média')
else:
    print('Abaixo da média')

# Desafios adaptados
aleatorio = random.randint(1,5)
palpite = int(input('De um palpite: \n'))

if palpite == aleatorio:
    print("Você acertou")
else:
    print("Você errou. O número era {}".format(aleatorio))

velocidade = int(input("Insira a velocidade do carro:\n"))
if velocidade >= 80:
    multa = (velocidade - 80 )*7
    print('Você foi multado em {} reais'.format(multa))
else:
    print("Você não foi multado")

numeroParImpar = int(input("Insira um número: \n"))
if numeroParImpar%2 == 0:
    print("O número é par")
else:
    print("O número é impar")

distanciaViagem = float(input('Qual a distância da viagem? (em Km)\n'))
if distanciaViagem <= 200:
    print("O custo da viagem é {}".format(distanciaViagem*0.50))
else:
    print("O custo da viagem é {}".format(distanciaViagem*0.45))

ano = int(input("Insira o ano:\n"))
if ano%4 == 0 and ano%100 != 0 or ano%400 == 0):                          
    print("É ano bissexto")
else:
    print("Não é ano bissexto")

num1 = int(input("Insira o número 1: \n"))
num2 = int(input("Insira o número 2: \n"))
num3 = int(input("Insira o número 3: \n"))

if num1 > num2 > num3:
    print("O maior numéro é {}, e o menor é {}".format(num1, num3))
elif num1 > num3 > num2:
    print("O maior numéro é {}, e o menor é {}".format(num1, num2))
elif num2 > num1 > num3:
    print("O maior numéro é {}, e o menor é {}".format(num2, num3))
elif num2 > num3 > num1:
    print("O maior numéro é {}, e o menor é {}".format(num2, num1))
elif num3 > num1 > num2:
    print("O maior numéro é {}, e o menor é {}".format(num3, num2))
else:
    print("O maior numéro é {}, e o menor é {}".format(num3, num1))

salarioAtual = float(input("Qual o seu salário atual?\n")) # Com f-string

if salarioAtual > 1250.00:
    salarioAtual = salarioAtual + (salarioAtual/10) # Atualiza salário
    print(f"Seu novo salário é {salarioAtual:.2f}")
else: 
    salarioAtual = salarioAtual + (salarioAtual/15)
    print(f"Seu novo salário é {salarioAtual:.2f}")

l1 = input("Primeira lado do triângulo: \n")
l2 = input("Segundo lado do triângulo: \n")
l3 = input("Terceiro lado do triângulo: \n")

if l1 > l2 + l3 or l2 > l1 + l3 or > l3 > l1 + l2:
    print("É um triângulo possível")
else:
    print("Não é um triângulo possível")