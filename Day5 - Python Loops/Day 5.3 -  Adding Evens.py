num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
sum = 0
#for n  in range( 1 , 10 , 2 ): third number is steps / jumps
for n  in range(num1 , num2+1 ): # add 1 to num2 so that it also include last digit
    if n%2==0:
      sum += n
print(f"Sum of all Even numbers between {num1} and {num2} is equal to {sum}")