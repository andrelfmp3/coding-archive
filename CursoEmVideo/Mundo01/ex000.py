#"Hello word" and basic concepts about python

print('Hello word') #todos comandos são funções

print(1)
print("1")

print(1+1) #imprime dado numérico. 
print('1'+'1') #concatena, portanto, imprime string

# print("Hello" + 5), gera erro, "+" é apenas para duas strings
print("Hello" + "5")
print("Hello", 5) #",", pois concatena string e inteiro

#-----------------------------------------------------------------------------------------

nome = "andre" #em python, toda variavel é um objeto
idade = 20
print(nome, idade);

nome = input("Qual o seu nome? \n")
print("Muito prazer",nome)

# " print(f"Muito prazer {nome}") "
# método com f-string, onde se adiciona o prefixo f oantes da string e usa-se chaves {}. 

nome2 = input("Qual o seu nome?\n")
print("Muito prazer,", nome2)

dia = input("Dia que você nasceu: ")
mês = input("Mês que você nasceu: ")
ano = input("Ano que você nasceu: ")

print("Você nasceu dia", dia + " de", mês + " de" , ano + " certo?") # "," faz espaçamento. apenas complementar

num1 = input("Número 1: ")
num2 = input("Número 2: ")
print(num1 + num2) #não faz soma, imprime um ao lado do outro
