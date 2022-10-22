# defining functions
def callHello():
    s1 ="Hello"
    s2 =" World"
    greeting = s1 + s2
    print(greeting)
#calling functions
callHello()

#while loop
number = 0
while number < 10:
    print(number)
    number += 1



#Reeborg World gaming challenge practice codes

#maze challenge and hurdles 1, 2, 3, 4 codes
def right():
    turn_left()
    turn_left()
    turn_left()
def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    right()
    move()
    right()
    while front_is_clear():
        move()
    turn_left()
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear() == True:
        right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()