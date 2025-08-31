# Notas sobre tipos primitivos e exercícios básicos

num1 = input('Número 1: ')
num2 = input('Número 2: ')
print('A soma com o tipo primitivo não específicado entre o número {} e o número {} é {}'.format(num1, num2, num1+num2))
# Específica tipo primitivo
num3 = int (input("Numero 3: ")) 
num4 = int (input("Numero 4: "))
print('A soma com o tipo primitivo específicado entre o número {} e o número {} é {}'.format(num3, num4, num3+num4))

# Em python, os tipos primitivos são int, float, bool (nativo) e str (string). sem Char (tipo de string)

# Saída formatada: SINTAXE PYTHON 3
soma = num3 + num4 # Possuem tipo primitivo especificado
print('\n A soma do número 3 e 4 vale {} \n'.format(soma))

print(type(num2)) # Retorna <class 'str'> (não específica == string?)
print(type(num3)) # Retorna <class 'int'> (específicada)

teste = bool(input('Digite um valor: \n'))
print('{}'.format(teste))
# Se inserir, retorna True; se deixar vazio, retorna False

teste2 = input('Digite algo: \n')
# Usando métodos com atributos para fins didáticos.

print(teste2.isnumeric()) # Se puder ser convertido pra número, retorna true
print(teste2.isalpha()) # Se for "ALPHAbético", retorna true
print(teste2.isalnum()) # Se for alphanumérico, retorna true
print(teste2.isupper()) #Verifica se é maiusculo
print(teste2.islower()) #Verifica se é minusculo


# Exercicico 3
# Programa que lê dois número e mostre a some entre eles

num5 = int(input('Insira o número 1: '))
num6 = int(input('Insira o número 2: '))
print('A soma dos número é {}.'.format(num5+num6))
