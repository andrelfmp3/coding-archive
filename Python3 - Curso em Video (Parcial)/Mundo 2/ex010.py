# Estrutura de condições aninhadas (if, elif, else)

nome = str(input('Qual seu nome? \n'))
if nome == 'Pedro':
    print("Pedro é o nome masculino mais comum no Brasil")
elif nome == 'Ana':
    print('Ana é o nome feminino mais comum no Brasil')
else:
    print("{} não é tão comum".format(nome))

# Exercicios
valorCasa = float(input("Qual o valor da casa? \n"))
salário = float(input("Qual o salário do morador? \n"))
anos = int(input("Tem que pagar por quantos anos? \n"))

prestacaoMensal = valorCasa / (anos*12)

if prestacaoMensal > (valorCasa * 0.30):
    print("Você não pode comprar está casa")
else:
    print("A prestação mensal é {:.2f}".format(prestacaoMensal))

valorQualquer = float(input('Escreva um valor qualquer: \n'))
base = int(input("Escreva a base de conversão (1 para binário, 8 para octal, 16 para hexadecimal): \n"))


if base == 1:
    print("{} em binário é {}".format(valorQualquer, bin(int(valorQualquer))))
elif base == 8:
    print("{} em octal é {}".format(valorQualquer, oct(int(valorQualquer))))
elif base == 16:
    print("{} em hexadecimal é {}".format(valorQualquer, hex(int(valorQualquer))))
else:
    print("Valor não reconhecido")