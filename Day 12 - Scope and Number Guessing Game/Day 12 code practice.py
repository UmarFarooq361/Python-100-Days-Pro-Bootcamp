apples = 10 #global scope 

banana = 12
def count():
    global apples
    apples += 14  #local scope inside the function
    peach = 4
    print(f"Number of apples in side the funcion is {apples}")
    print(f"Number of banana declared outside the funcion  is {banana}")

print(f"Number of apples outside the funcion is {apples}")
# print(f"Number of peach that is declared in the count funcion is {peach}") #error as peach is local variable
count()

#there is no block scope
level = 3
if level < 10:
    new_level = 4
print(new_level)  #new_level is not in function . so it is accessible