# Data types

#1 String data types
print("Hello coder")
print("Hello coder"[0]) # this is known as subscript it print character at that index

#2 intergers
print(12+4)

#3 float : number contain decimal point
print(1.2+7.44)

 #4 boolean : True or False

 #type of data and convertion of these types
name = input("What is the name ? \n")
print(type(name))
new_name = str(len(name)) #it will convert interger into string value
print("Your name has " + new_name + " characters " )

print(40 + int("322"))
print(40 + float("3.22"))
print("my number is " + str(322))

#code challenge 2.1
number = input("Enter two digit number : ")
print(int(number[0]) + int(number[1]))

#round decimal and devision

print(round(8/3,2)) #this will round of to 2 decimal places
print(8//3) # this will simply convert float to integer

# f-string  # this makes easy . we dont need to convert data types to be same for printing
score = 5
win = True
print(f"your score is {score} and your winning is {win}")

# challenge 2.3 : how much time you have left
currentAge = input("Enter your age : ")
currentAge = int(currentAge)
age = 90
days = 365
months = 12
weeks = 52
left_years = age-currentAge
print(f"You left with {days*left_years} days ,"
      f" {weeks*left_years} weeks and {months*left_years} months in your life if you live for 90 years ")



