# Exercício 4
# Faça um programa que leia algo pelo teclado e mostre na tela o tipo primitivo e todas informações possíveis

info = input('Insira qualquer informaçâo: ')
print('Está informação é classificada como: " {} ", onde se tem as seguintes informações: '.format(type(info)))

print('É um número?: ', info.isdigit())
print('É alfanumérico?: ', info.isalnum())
print('É ASCII?: ', info.isascii())
print('É composto apenas de espaços?: ', info.isspace())
print('É um número decimal?: ', info.isdecimal())
print('É imprimível?: ', info.isprintable())
print('É uma representação de números ou caracteres em ASCII?: ', info.isascii())

