def greet():
    print("hello coder")

greet()

def greet_with_name(name):
    print(f"hello {name}")

greet_with_name("umar")

#multiple parameters
def greet_with(name,location):
    print(f"hello {name}")
    print(f"Your location is  {location}")

greet_with("farooq","lahore")

# functions with keyword parameter  : its helps to not mix the multiple parameters 
def greet_with(name,location):
    print(f"hello {name}")
    print(f"Your location is  {location}")

greet_with(location="rawalpindi" , name = "hamza")
