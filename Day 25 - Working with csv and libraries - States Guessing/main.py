import turtle
import pandas
screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states50 = pandas.read_csv("50_states.csv")
listOfStates = states50.state.to_list()
guessList = []


# print(title_answer)
while len(guessList)<50:
    answer = turtle.textinput(title=f"{len(guessList)}/50 States Corrert", prompt="Enter name of U.S states")
    title_answer = answer.title()
    if title_answer == "Exit":
        missingStates = [state for state in listOfStates if state not in guessList]
        # this code is without the concept of comprehension
        # missingStates = []
        # for state in listOfStates:
        #     if state not in guessList:
        #         missingStates.append(state)
        missing_data = pandas.DataFrame(missingStates)
        missing_data.to_csv("StatesToLearn2.csv")
        break;
    if title_answer in listOfStates:
        if title_answer not in guessList:
            guessList.append(title_answer)
        state_data = states50[states50.state == title_answer]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        x_axis = int(state_data.x)
        y_axix = int(state_data.y)
        t.goto(x_axis , y_axix)
        t.write(title_answer)


