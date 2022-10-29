# practice of conditions like if elif else
num = int(input("Enter your height ? "))

if num>=120:
    age = int(input("Enter your age ? "))
    if age < 12:
       print("You have to pay $2")
    elif age <=18:
        print("You have to pay $5")
    else:
        print("You have to pay $8")

else:
    print("Your are not allowed to ride")
