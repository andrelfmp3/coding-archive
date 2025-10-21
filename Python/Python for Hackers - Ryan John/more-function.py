# functions

ip = "10.10.10.10"
url = "domain.com"

def attack(a, b):
    print(f"Target ip is {a} and the domain is {b}")
    # pass # sem erro de sintaxe

attack("10.10.10.10", "domain.com")
attack(ip, url)

print("-" * 100)

print("Insira o valor: ")

def calculate_area(w,h):
    area = w * h
    print(f"A area é {area}")
    
w = int(input("Width: "))
h = int(input("Height: "))

calculate_area(w, h)

