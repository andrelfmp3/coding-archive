preco = float(input("Qual o valor da casa? \n"))
sal = float(input("Qual é o seu salário? \n"))
tempo = int(input("Em quantos anos você vai pagar? \n"))

mensalidade = (preco / (tempo * 12))

print("Valor da casa: {:.2f}".format(preco))
print("Prestação: {:.2f}".format(mensalidade))

if mensalidade >= (sal * 30 / 100):
    print("Empréstimo negado.")
else:
    print(f"Mensalidade durante {tempo} anos: R${mensalidade}")
    
    
num = int(input("Digite um número a ser convertido: \n"))
base = int(input('''Escolha a base da conversão:
Para binário digite: 1
Para octal digite: 2
Para hexadecimal digite: 3

Sua escolha: \n'''))

if base == 1:
    print("{}".format(bin(num)[2:])) # fatia = corta dois primeiros caracteres
elif base == 2:
    print("{}".format(oct(num)[2:]))
elif base == 3:
    print("{}".format(hex(num)[2:]))
else:
    print("Opção inválida")
    
    
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

if num1 > num2:
    print("O primeiro valor é maior")
elif num2 > num1:
    print("O segundo valor é maior")
else:
    print("Iguais.")
    
    
from datetime import datetime # pegar datas pelo sistema

nasc = int(input("Em qual ano você nasceu? \n"))
ano_atual = datetime.now().year # importa ano atual do sistema
idade = (ano_atual - nasc)
if idade < 18:
    print("Vai se alistar")
elif idade > 18:
    print("Já passou seu período de alistamento")
else:
    print("Hora de se alistar!")
    
    
n1 = float(input("Nota 2: "))
n2 = float(input("Nota 1: "))
m = ((n1 + n2) / 2)

if m < 5.0:
    print("REPROVADO.")
elif m > 6.9:
    print("APROVADO")
else:
    print("RECUPERAÇÃO.")
    
    
a = float(input("Primeiro segmento de reta: "))
b = float(input("Segundo segmento de reta: "))
c = float(input("Terceiro segmento de reta: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("O triângulo que existe é um", end="") # não quebra linha
    if a == b == c:
        print(" equilátero.")
    elif (a == b) or (a == c) or (b == c):
        print(" isosceles.")
    else:
        print(" escaleno.")
else:
    print("O triângulo não existe.")
    
    
from random import choice

choices_list = ["pedra", "papel", "tesoura"]

print("Pedra, Papel, Tesoura!")

escolha = str(input("Você escolhe pedra, papel ou tesoura? \n")).lower()

def judge(computador, player):
    print(f"""
    Jogador: {escolha}
    Computador: {computador}
    """
    )

    if computador == player:
        return print("Empate.")

    if escolha == "pedra" and computador == "tesoura":  # Pedra x Tesoura: Pedra
        return print("Jogador ganhou.")

    if escolha == "tesoura" and computador == "pedra":  # Tesoura x Pedra: Pedra
        return print("Computador ganhou.")

    if escolha == "papel" and computador == "pedra":  # Papel x Pedra: Papel
        return print("Jogador ganhou.")

    if escolha == "pedra" and computador == "papel":  # Pedra x Papel: Papel
        return print("Computador ganhou.")

    if escolha == "papel" and computador == "tesoura":  # Papel x Tesoura: Tesoura
        return print("Computador ganhou.")

    if escolha == "tesoura" and computador == "papel":  # Tesoura x Papel: Tesoura
        return print("Jogador ganhou.")


judge(choice(choices_list), escolha)
    