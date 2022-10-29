def add(num1 , num2):
    return num1 + num2
def subtract(num1 , num2):
    return num1 - num2
def multiply(num1 , num2):
    return num1 * num2
def devide(num1 , num2):
    return num1 / num2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : devide
}
def calculator():
    should_continue = True
    num1 = float(input("Enter first number : "))
    for key in operations:
        print(key)
    while should_continue:
        operation = input("Pick a operation : ")
        num2 = float(input("Enter next number : "))
        output = (operations[operation](num1, num2))
        print(f"{num1} {operation} {num2} = {output}")
        if input(f"Type 'y' to continue with the {output} or 'n' to start new calculation : ") == "y":
            num1 = output
        else:
            should_continue = False
            calculator()

calculator()