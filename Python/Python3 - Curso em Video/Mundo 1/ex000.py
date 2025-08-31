#"Hello word" and basic concepts about python

print('Hello word') # Todos comandos são funções. Comunidade usa aspas simples para strings.

print(1)
print('1')

print(1+1) # Imprime dado numérico. 
print('1'+'1') # Concatena, portanto, imprime string

# " print("Hello" + 5) " gera erro, " + " é apenas para duas strings
print('Hello' + '5')
print('Hello', 5) # ",", pois concatena string e inteiro

#-----------------------------------------------------------------------------------------

nome = 'andre' # Em python, toda variavel é um objeto
idade = 20
print(nome, idade);

nome2 = input('Qual o seu nome?\n')
print('Muito prazer,', nome2)
print(f"Muito prazer {nome2}") # Método com f-string, onde se adiciona o prefixo f oantes da string e usa-se chaves {}. 

dia = input('Dia que você nasceu: ')
mês = input('Mês que você nasceu: ')
ano = input('Ano que você nasceu: ')

print('Você nasceu dia', dia + ' de', mês + ' de' , ano + ' certo?') # "," faz espaçamento. apenas complementar


