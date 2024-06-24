# Manipulação de String

frase = 'Curso em Video Python'
# Anexa caracteres na memória do computador
# Espaço é caractere

# Operações:
# 'Fatiamento'
frase[15] # lista, apenas caractere "P"
frase[15:21] # "Python", caracteres 15 até 21
frase[9:21:2] # 9 até 20, pulando de 2 em 2. VdoPto
frase[:5] # equivalente a frase[0:5], indo de 0 até 4
frase[15:] # da casa 15 até o final
frase[9::3] # de 9 até o final, pulando 3 casas a cada caractere.

# Análise
len(frase) # lenght, retorna QUANTIDADE de caracteres, conta zero.
frase.count('o') # retorna quantas vezes 'o' aparece na string 
frase.count('0',0,13) # procura "0" de 0 até 12
frase.find("deo") #retorna em que momento COMEÇOU deo. Retorna -1 se não existir

'deo' in frase # equivalente, mas operador. Retorno booleano

frase.replace('python', 'android') # substitui, mas não diretamente
frase.upper() # deixa tudo em maisculo 
frase.lower() # deixa tudo em minusculo
frase.capitalize() # deixa tudo em minusculo, menos primeiro caractere. "Curso em video python"
frase.tittle() # deixa todo começo de frase maiusculo, e resto minusculo. "Curso Em Video Python"
frase.strip # remove espaços inuteis no começo e fim da string.

frase.lstrip # apenas left
frase.rstrip # apenas right

# Divisão
frase.split() # fivide onde tem espaços. Gera lista de palavras
# Junção
'-'.join(frase) # Retorna "curso-em-video"

# nao finalizado, minuto 29:35







