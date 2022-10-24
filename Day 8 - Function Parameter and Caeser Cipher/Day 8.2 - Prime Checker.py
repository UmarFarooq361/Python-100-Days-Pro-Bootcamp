num = int(input("Enter the number : "))

def prime_checker(number):
    is_prime = True
    for n in range(2 , number):
        if number % n == 0:
            print("Its not a prime number")
            is_prime = False
            break
    if is_prime:
        print("Its a prime number")
prime_checker(number = num)