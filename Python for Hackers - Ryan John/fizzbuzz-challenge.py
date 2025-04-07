num = int(input("Your number: "))

if num % 5 == 0 and num % 3 == 0:
    print("Fizzbuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)    
