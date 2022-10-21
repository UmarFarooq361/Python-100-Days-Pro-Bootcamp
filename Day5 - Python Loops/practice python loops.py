fruits = ["apple" , "mango" , "banana"]
for i in fruits:
    print(i)
print(fruits)

# for loop with range functions
num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
sum = 0
for n  in range(num1 , num2+1): # add 1 so that it also include last digit
    sum += n
print(f"Sum of number between {num1} and {num2} is equal to {sum}")