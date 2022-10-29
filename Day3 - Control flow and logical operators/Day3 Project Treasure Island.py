print('''
      
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   |
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.|uuu|.-'    __/ \__ |
              |==== .'.'^'.'.====|
              |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`


''')

print("Welcome to the Treasure Island.")
print("Your mission is to find treasure .")
choice1 = input('you\'re at across the road . where do you want to go? "Left" or "Right" ? ').lower()

if choice1== "left":
    choice2 = input('you\'ve come to a lake .The island is middle of the ocean . Type "Wait" to wait for boat'
                    'or "swim" to go by yourself').lower()
    if choice2 == "wait":
        choice3 = input('you\'ve arrived saftly at island . There are 3 doors "red" , "blue"'
                        '"green" . Which colour you want to choose').lower()
        if choice3 == "red":
            print("The room is full of fire . Game Over!")
        elif choice3 == "green":
            print("Congtats you found a treasure . YOU WON!")
        elif choice3 == "blue":
            print("The room is full of beast . Game Over!")
        else:
            print("The door does not exist . Game Over!")
    else:
        print("You got attack by angry shark . Game Over!")
else:
    print("You fell into hole . Game Over!")