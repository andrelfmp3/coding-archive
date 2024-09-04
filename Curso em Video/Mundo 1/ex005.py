# operadores aritméticos

#  + para soma, - para subtração
#  * para multiplicação, / para divisão
# ** para potência (ou pow() ), == para igualdade 
    # raiz de x = potencia de 1/x
# // para divisão inteira, % para resto da divisão

# Procedência: (); **; *, /, //, %: +, -

print(365**522) # limite é memória da máquina
print("\n") # alinhar código

print("5vezes"*5) # imprime string 5x

nome = input('\nQual seu nome? \n')
print('Nome: {}! '.format(nome))
print('Nome alinhado a direita: {:>20} !'.format(nome)) 
print('Nome alinhado a esquerda: {:<20} !'.format(nome)) 
print('Nome alinhado centralizado: {:^20} !'.format(nome)) 
print('Nome alinhado centralizado com "-": {:-^20} !\n'.format(nome))

print("começo")
print(" e fim\n")

print("começo", end='')
print(" e fim\n")

print("começo\n e fim\n\n")

# Desafios em aula adaptados
valor = float(input("Insira um número inteiro: \n"))
print("Seu antecessor é {:.2f} e seu sucessor é {:.2f}".format(valor-1,valor+1))
print("Seu dobro é {:.2f}, seu triplo é {:.2f} e sua raiz quadrada é {:.2f}".format(valor*2,valor*3,valor**0.5))
print("A média do valor com o dobro dele é {:.2f}".format((valor+(valor*2))/2))
print("15% a mais do valor é {:.2f}".format(valor + ((valor/100)*15)))
print("15% a menos do valor é {:.2f}".format(valor - ((valor/100)*15)))
print("Sendo {:.2f} metros, possui {:.2f} centímetros e {} milimetros".format(valor, valor*100, valor*100000))
print("Sua tabuada é (sem for): {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}, ".format(valor*1, valor*2, valor*3, valor*4, valor*5, valor*6, valor*7, valor*8, valor*9, valor*10))
