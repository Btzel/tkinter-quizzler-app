from data import QuestionRequester
from tkinter import messagebox

class QuizBrain(QuestionRequester):
    def __init__(self):
        super().__init__()
        self.question_number = 0
        self.question_number_holder = 0
        self.question_list = self.get_question_bank()

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.question_number_holder += 1
        return current_question

    def check_answer(self,user_answer,correct_answer,score,window):
        if correct_answer.lower() == user_answer.lower():
            score += 1
            is_right = True
        else:
            is_right = False

        if not self.still_has_questions():
            will_continue = messagebox.askyesno(title="We're done with questions!",message="If you want to continue playing, press yes")
            if will_continue:
                messagebox.showinfo(title="Info.", message="Next questions are on the way :)")
                self.get_new_questions()
            else:
                messagebox.showinfo(title="Thank you for playing!", message=f"Your final score is {score} out of {self.question_number_holder}")
                window.quit()

        return score,is_right

    def get_new_questions(self):
        self.question_list.clear()
        self.question_number = 0
        self.question_list = self.get_question_bank()





