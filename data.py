from question_model import Question
import requests

class QuestionRequester:
    def __init__(self):
        self.question_bank = []

    @staticmethod
    def ask_for_question():
        response = requests.get("https://opentdb.com/api.php?amount=20&type=boolean")
        response.raise_for_status()
        if response.json()['response_code'] == 0:
            return response.json()['results']
        else:
            print("Trouble while requesting questions")
            return None

    def create_question_bank(self):
        question_data = self.ask_for_question()
        if question_data is not None:
            for question in question_data:
                question_category = question['category']
                question_difficulty = question['difficulty']
                question_text = question['question']
                question_answer = question['correct_answer']
                new_question = Question(question_category, question_difficulty, question_text, question_answer)
                self.question_bank.append(new_question)

    def get_question_bank(self):
        self.clear_question_bank()
        self.create_question_bank()
        return self.question_bank

    def clear_question_bank(self):
        self.question_bank.clear()
