# Utilizando módulos (Adicionar Funcionalidades)

# Maneiras de importar funcionalidades:
import math # importa todo operadores, generalista
from math import pow, sqrt # importa apenas pow e sqrt, específico
# (Neste caso, redundante, pois pow e sqrt estão inclusos em math)

num1 = int(input('Digíte um número: '))
raiznum1 = math.sqrt(num1) # raiz = sqrt(num1), caso não importe a math inteiro
print("A raiz de {} é igual a {}".format(num1, raiznum1))

# Exercícios Adaptados:
num2 = float(input('Digite um número flutuante: '))
inteironum2 = math.trunc(num2)
print("A parte inteira de {} é {}".format(num2, inteironum2))

print("Considere um triangulo retángulo com todos os comprimentos inteiros")
num3 = int(input('Insira o cateto oposto: '))
num4 = int(input('Insira o cateto adjacente: '))
hipotenusa = sqrt((pow(num3, 2)) + (pow(num4, 2)))
print("A hipotenúsa é {}".format(hipotenusa))

num5 = float(input("Insira um ângulo: "))
sen = math.sin(math.radians(num5))
cos = math.cos(math.radians(num5))
tan = math.tan(math.radians(num5))

print("o seno do angulo é {:.4f}".format(sen))
print("o cos do angulo é {:.4f}".format(cos))
print("o tan do angulo é {:.4f}".format(tan))

print("Insira os quatro nomes para serem sorteados: \n")
nome1 = str(input('Insira o nome 1: '))
nome2 = str(input('Insira o nome 2: '))
nome3 = str(input('Insira o nome 3: '))
nome4 = str(input('Insira o nome 4: '))
lista = [nome1, nome2, nome3, nome4]
from random import choice, shuffle
sorteado = choice(lista) # Considera como um Array
print('O sorteado foi {}'.format(sorteado))

shuffle(lista)
print('A ordem de outro sorteio foi foi: {}'.format(lista))

import playsound
playsound.playsound('/home/andrelf/Documents/GitHub/python-exercises/Mundo 1/ex006.mp3')
