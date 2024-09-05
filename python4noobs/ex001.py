# Estrutura de dados

string1 = 'Olá mundo'
string2 = "H4rtDevs é maior grupo de devs do Brasil"
string3 = """Nossa, bem grande essa string..."""

print(type(string1))
print(type(string2))
print(type(string3))

string4 = 123
string5 = "123"

print(type(string4)) # Retorna int
print(type(string5))

string6 = "Python é" + " muito " * 2 + " simples" 
print(string6)

string7 = ".py" # Pode ser acessado de "trás para frente"

print(string7[0] + string7[1] + string7[2]) # 0 + 1 + 2
print(string7[-3] + string7[-2] + string7[-1]) # -3 + -2 + -1

string8 = "12caracteres"
print(f"A string tem {len(string8)} caracteres")
print(f"O caractere '{string8[3]}' se repete {(string8).count(string8[3])} vezes")

string9 ='python'
print(string9[1:5]) # Entre 1 e 5
print(string9[:4]) # Até o caractere[4] 
print(string9[1:5]) # Entre 1 e 5
print(string9[0:5:2]) # De 0 é 5. De 2 em 2;

# Num complexo. J = imaginário.
num1 = 4
print(type(num1))
print(complex(num1)) 

# // = divisão inteira
# ** = exponenciação

