
# from mainFile import question_bank
class QuizBrain:
    def __init__(self , question_bank):
        self.question_no = 0
        self.score = 0
        self.question_list = question_bank

    def still_has_question(self):
        if self.question_no< len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.question_list[self.question_no]
        self.question_no += 1
        ans = input(f"Q. {self.question_no} : {current_question.text} . (True / False)? ")
        self.check_answer(ans , current_question.answer)

    def check_answer(self , user_answer , correct_answer ):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right! ")
        else:
            print("You are wrong! ")
        print(f"Correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_no}")