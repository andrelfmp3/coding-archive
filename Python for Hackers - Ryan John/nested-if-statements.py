score = int(input("What was your test score? "))

if score >= 90:
    age = int(input("What is your age? ")) # existed only here
    if age < 10:
        print("Your grade is an A+")
    else: 
        ("Your grade is an A")
elif score >= 80:
    age = int(input("What is your age? "))
    if age < 10:
        print("Your grade is an B+")
    else: 
        ("Your grade is an B")
elif score >= 970:
    print("Your grade is an C")
else:
    print("You are dumb")

    
# pseudo switch-case = match-case.

def http_error(status): # py 3.10 doc
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        