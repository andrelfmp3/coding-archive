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

# exercicios nao finalizados 
