# Manipulação de String

frase = 'Curso em Video Python'
# Anexa caracteres na memória do computador
# Espaço é caractere

# Operações:
# 'Fatiamento'
print(frase[15])      # lista, apenas caractere "P"
print(frase[15:21])   # "Python", caracteres 15 até 20
print(frase[9:21:2])  # 9 até 20, pulando de 2 em 2. VdoPto
print(frase[:5])      # equivalente a frase[0:5], indo de 0 até 4
print(frase[15:])     # da casa 15 até o final
print(frase[9::3])    # de 9 até o final, pulando 3 casas a cada caractere.

# Análise
print(len(frase))               # length, retorna QUANTIDADE de caracteres, conta zero.
print(frase.count('o'))         # retorna quantas vezes 'o' aparece na string 
print(frase.count('o', 0, 13))  # procura "o" de 0 até 12

print(frase.find("deo"))        # retorna em que momento COMEÇOU "deo". Retorna -1 se não existir
print('deo' in frase)           # equivalente, mas operador. Retorno booleano

print(frase.replace('Python', 'Linux'))  # substitui "Python" por "Linux", mas não altera a string original
print(frase.upper())            # deixa tudo em maiúsculo 
print(frase.lower())            # deixa tudo em minúsculo
print(frase.capitalize())       # deixa tudo em minúsculo, menos o primeiro caractere. "Curso em video python"
print(frase.title())            # deixa o começo de cada palavra em maiúsculo, e o resto minúsculo. "Curso Em Video Python"
print(frase.strip())            # remove espaços inúteis no começo e no fim da string.

print(frase.lstrip())           # remove espaços à esquerda
print(frase.rstrip())           # remove espaços à direita

# Divisão
print(frase.split())            # divide onde há espaços. Gera lista de palavras

# Junção
print('-'.join(frase.split()))  # Retorna "Curso-em-Video-Python"

# Exemplos adicionais:
print(frase)
print(frase[:14])
print(frase[0:15:2])            # Pula de 2 em 2
print("""
imprime
texto
inteiro""")
print(len(frase))               # Tamanho da frase
print(frase.replace('Python', 'Linux'))  # Substituição, mas apenas na instância
print('Curso' in frase)         # Verifica se 'Curso' está na string
print(frase.find("Python"))     # Índice da primeira ocorrência de "Python"

print(frase.split())
lista = frase.split()
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
print(lista[0][0])
print(lista[1][0])
print(lista[2][0])
print(lista[3][0])

# Desafios Adaptados:
NomeCompleto = input('Qual o seu nome completo?\n')
print('\n')
print("Nome completo maiúsculo: {}".format(NomeCompleto.upper()))
print("Nome completo minúsculo: {}".format(NomeCompleto.lower()))
print(len(NomeCompleto))                    # Com espaços
print(len(NomeCompleto.replace(' ', '')))  # Sem espaços
listaNomeCompleto = NomeCompleto.split()
print(len(listaNomeCompleto[0]))
print("Nome: {}".format(listaNomeCompleto[0]))
print("Sobrenome: {}".format(listaNomeCompleto[1]))  # Corrigido para a formatação correta

Numero = input('Digite um número: \n') 
NumeroComZero = Numero.zfill(4)           # Preenche com zero para a esquerda
print("Unidade: {}".format(NumeroComZero[3]))
print("Dezena:  {}".format(NumeroComZero[2]))
print("Centena: {}".format(NumeroComZero[1]))
print("Milhar:  {}".format(NumeroComZero[0]))

cidade = input("Insira a cidade:\n")
cidadeFormatada = cidade.lower()
listaCidades = cidadeFormatada.split()

if "santo" == listaCidades[0]:           # Adaptado com estrutura de condição
    print("Começa com Santo")
else:
    print("Não começa com Santo")

nome = input("Insira o nome completo:\n")
nomeFormatado = nome.lower()

if "silva" in nomeFormatado:             # Adaptado com estrutura de condição
    print('Tem Silva')
else:
    print("Não tem Silva")

frase = input("Insira uma frase qualquer:\n")
fraseFormatada = frase.upper()
print("Quantos 'R' tem? {}".format(fraseFormatada.count("R")))
print("Qual o primeiro 'R'? {}".format(fraseFormatada.find("R") + 1))
print("Qual o último 'R'? {}".format(fraseFormatada.rfind("R") + 1))
