import time

def function(choice):
    for num in range(1, choice + 1):
        if num % 5 == 0 and num % 3 == 0:
            print("Fizzbuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)    

choice = int(input("What number would you like to choose?: "))

print("About to run program.", end="") # não quebra mais a linha por padrão
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
function(choice)

ip = input("What is the target ip address? ")

def nmap(ip):
    print(f"The ip \"{ip}\" is the target.")
    
nmap(ip)
            