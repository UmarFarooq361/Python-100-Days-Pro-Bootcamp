import random
#random number generator
random_int =  random.randint(0,15)
print(random_int)

#float random number
random_float =  random.random()  #number between 0 to 0.9999999999999...
print(random_float)

score =  random.randint(0,100)
print(f"Your love score is {score}")

# List - Type of Data structues

fruit = ["apple" , "banana"]
print(fruit[1])
fruit.extend(["orange","mango"])
print(fruit)
print(fruit[-1]) #this will print from last value

# nested lists
fruit = ["apple" , "banana"]
vegetable = ["kale" , "tamatos"]
mix_veg = [fruit , vegetable]
print(mix_veg)