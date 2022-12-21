import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title.config(text="Timer ", fg=GREEN)
    # time_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 34, "bold"), fill="white")
    # time_text.config(canvas.create_text(100 , 130 , text= "00:00" , font=(FONT_NAME, 34, "bold") , fill = "white"))
    canvas.itemconfig(time_text , text = "00:00")
    tick.config(text= "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_count():
    global reps
    reps += 1
    work_time = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        count_down(long_break)
        title.config(text="Break", font=(FONT_NAME, 32), fg=PINK, bg=YELLOW)

    elif reps % 2 == 0:
        count_down(short_break)
        title.config(text="Break", font=(FONT_NAME, 32), fg=RED, bg=YELLOW)

    else:
        count_down(work_time)
        title.config(text="Work ", font=(FONT_NAME, 32), fg=GREEN, bg=YELLOW)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min_left = math.floor(count / 60)
    sec_left = count % 60
    if sec_left<10:
        sec_left = f"0{sec_left}"
    display_time = f"{min_left}:{sec_left}"
    canvas.itemconfig(time_text , text = display_time)
    if count>0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_count()
        mark = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            mark += "✔"
            tick.config(text= mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro App")
window.config(padx=100 , pady=110, bg= YELLOW)

canvas = Canvas(width= 200 , height= 224 , bg= YELLOW)
bg_img = PhotoImage(file = "tomato.png")
canvas.create_image(102 , 112 , image = bg_img)
time_text = canvas.create_text(100 , 130 , text= "00:00" , font=(FONT_NAME, 34, "bold") , fill = "white")
canvas.grid(column=1, row=1)

title = Label(text= "Timer", font= (FONT_NAME, 35), fg = GREEN , bg= YELLOW)
title.grid(column=1, row=0)

start_btn = Button(text= "Start" ,font= (FONT_NAME, 18) , command=start_count)
start_btn.grid(column=0, row=2)
start_btn.config(pady= 2, padx=5 )

reset_btn = Button(text= "Reset" ,font= (FONT_NAME, 18), command= reset_timer)
reset_btn.grid(column=2, row=2)
reset_btn.config(pady= 2, padx=5 )

tick = Label( fg = GREEN, font= (FONT_NAME, 24))
tick.grid(column=1, row=3)


window.mainloop()