#game that print number but if number divisible by 3 it will print FIZZ if its divisible by 5
#then it will print BUZZ , if both are divisible then FIZZBUZZ will be printed
for n  in range(1 , 101 ):
    if n%3==0 and n%5==0 :
      print("FizzBuzz")
    elif n%3==0:
      print("Fizz")
    elif n%5==0:
      print("Buzz")

    else:
        print(n)
