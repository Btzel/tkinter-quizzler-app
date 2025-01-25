from tkinter import *

from quiz_brain import QuizBrain
import html

THEME_COLOR = "#375362"


class Interface(QuizBrain):
    def __init__(self):
        super().__init__()

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = 0
        self.score_label = Label(
            text=f"Score: {self.score}",
            fg="white", bg=THEME_COLOR,
            font=("Arial",15,"normal")
        )
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_image = PhotoImage(file="./images/true.png")
        self.false_image = PhotoImage(file="./images/false.png")

        self.true_button = Button(
            image=self.true_image,
            highlightthickness=0,
            command=self.true_button_event
        )
        self.true_button.grid(column=0, row=2)
        self.false_button = Button(
            image=self.false_image,
            highlightthickness=0,
            command=self.false_button_event
        )
        self.false_button.grid(column=1, row=2)

        self.correct_answer = None
        self.show_question()
        self.window.mainloop()

    def show_question(self):
        if self.still_has_questions():
            self.canvas.config(bg="white")
            current_question = self.next_question()
            category = current_question.category.title()
            difficulty = current_question.difficulty.title()
            question_text = (f"Q.{self.question_number_holder}:"
                             f" {html.unescape(current_question.text)}")
            full_text = html.unescape(f"{category} | {difficulty}\n{question_text}")
            self.correct_answer = current_question.answer
            self.canvas.itemconfig(self.question_text, text=full_text)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def true_button_event(self):
        user_answer = "True"
        self.score,is_right = self.check_answer(user_answer, self.correct_answer, self.score, self.window)
        self.give_feedback(is_right)

    def false_button_event(self):
        user_answer = "False"
        self.score,is_right = self.check_answer(user_answer, self.correct_answer, self.score, self.window)
        self.give_feedback(is_right)


    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.update_score()

        self.window.after(500,self.show_question)

Interface()






