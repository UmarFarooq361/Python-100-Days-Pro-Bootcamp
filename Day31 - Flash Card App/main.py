from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
try:
   data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    french_words = pandas.read_csv("data/french_words.csv")
    to_learn = french_words.to_dict(orient="records")
else:
    new_learn = data.to_dict(orient= "records")

def flip_card():
    canvas.itemconfig(title, text="English" ,fill= "white")
    canvas.itemconfig(word, text=current_card["English"], fill= "white")
    canvas.itemconfig(canvas_img , image = new_img)

def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = to_learn[random.randint(0 , len(to_learn))]
    canvas.itemconfig(title, text="French", fill= "black")
    canvas.itemconfig(word, text=current_card["French"], fill= "black")
    canvas.itemconfig(canvas_img, image=old_img)
    flip_timer = window.after(3000, func= flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()





window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, background= BACKGROUND_COLOR )

flip_timer = window.after(3000, func= flip_card)


canvas = Canvas(width=800 , height= 530 , background= BACKGROUND_COLOR ,highlightthickness=0)
old_img = PhotoImage(file="images/card_front.png")
new_img = PhotoImage(file="images/card_back.png")
canvas_img = canvas.create_image(400 , 264, image= old_img , )
canvas.grid(column=0, row=0 , columnspan=2)
title = canvas.create_text(400, 150, text="Title", font=("arial", 40 , "italic"))
word = canvas.create_text(400, 258, text="Word", font=("arial", 60, "bold"))

cancel_btn_img = PhotoImage(file="images/wrong.png")
cancel_btn = Button(image= cancel_btn_img , highlightthickness=0, command= next_card)
cancel_btn.grid(column=0 , row=1)

ok_btn_img = PhotoImage(file="images/right.png")
ok_btn = Button(image= ok_btn_img , highlightthickness=0 , command= is_known)
ok_btn.grid(column=1 , row=1)

next_card()







window.mainloop()