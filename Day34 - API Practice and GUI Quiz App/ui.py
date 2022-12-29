THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizlet")
        self.window.config(padx=30, pady=30, background=THEME_COLOR)
        self.score_label = Label(text= "score", font= ("arial", 24), bg= THEME_COLOR, fg= "white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, background='white', highlightthickness=0)
        self.canvas.grid(column=0, row=1, columnspan= 2, pady= 50)
        self.question_text = self.canvas.create_text(150, 120,
                                                     width= 280,
                                                     text="Title",
                                                     font=("arial", 20, "italic"),
                                                     fill=THEME_COLOR)

        self.cancel_btn_img = PhotoImage(file="images/false.png")
        self.cancel_btn = Button(image=self.cancel_btn_img, highlightthickness=0, command= self.true_pressed)
        self.cancel_btn.grid(column=1, row=2)

        self.ok_btn_img = PhotoImage(file="images/true.png")
        self.ok_btn = Button(image=self.ok_btn_img, highlightthickness=0 , command= self.false_pressed)
        self.ok_btn.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.score_label.config(text= f"score : {self.quiz.score}")
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text= q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached to the end of quiz.")
            self.ok_btn.config(state="disabled")
            self.cancel_btn.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg= "green")
        else:
            self.canvas.config(bg= "red")
        self.window.after(1000, self.get_next_question)


