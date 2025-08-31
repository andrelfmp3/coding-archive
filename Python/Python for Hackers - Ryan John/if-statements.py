fnumber = input("First number: ")
snumber = input("Second number: ")

if fnumber > snumber:
    print("First number is bigger.")
elif snumber > fnumber:
    print("Second number is bigger.")
else:
    print("Same number")
    
score = int(input("What was your test score? "))

if score >= 90:
    print("Your grade is an A")
elif score >= 80:
    print("Your grade is an B")
elif score >= 970:
    print("Your grade is an C")
else:
    print("You are dumb")