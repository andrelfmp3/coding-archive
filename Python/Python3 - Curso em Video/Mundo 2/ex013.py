from time import sleep
from datetime import date

for contagem in range(5, -1, -1): # Inicio, Fim, Passo
    print(contagem)
    sleep(0.5)
print("New Year")

for n in range(2, 51, 2):
    print(n)

total = 0
for x in range(1, 501):
    if x % 2 != 0 and x % 3 == 0:
        total += x
print(f"Soma dos números ímpares múltiplos de 3: {total}")

num = int(input("Informe um número para ver a tabuada: \n"))
for i in range(1, 11):
    print(f"{num * i} ")

num_primo = int(input("Informe numero: \n"))
primo = True
for i in range(2, num_primo // 2 + 1):
    if num_primo % i == 0:
        primo = False
        break
if primo and num_primo > 1:
    print(f"{num_primo} é primo.")
else:
    print(f"{num_primo} não é primo.")

frase_input = input("Digite uma frase: \n").upper()
if frase_input == frase_input[::-1]: # 0 0 -1
    print("é um palíndromo.")
else:
    print("não é um palíndromo.")