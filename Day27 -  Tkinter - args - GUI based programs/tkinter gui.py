from tkinter import *

window = Tk()
window.minsize(width=500 , height= 400)
window.title( "GUI Program")
my_label = Label(text= "I am label", font= ("arial", 22))
my_label.pack()


def btn_click():
    # my_label["text"] = "Button got clicked"
    inputText = input.get()
    my_label.config(text=f"{inputText}")
my_btm = Button(text= "click me" , command= btn_click)
my_btm.pack()

input = Entry(width=15)
input.pack()


window.mainloop()

# class car:
#     def __init__(self, **kw):
#         self.model = kw["model"]
#         self.color = kw.get("color")
#
# my_car = car(model= "gt-r" , color="black")
# print(my_car.color)