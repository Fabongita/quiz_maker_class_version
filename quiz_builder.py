from quiz_question import QuizQuestion
import random

class QuizBuilder():
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.questions = []
    def add_question(self, correct_answer, wrong_answers, question):
        option_label = ["a", "b", "c", "d"]
        all_answers = [correct_answer] + wrong_answers
        random.shuffle(all_answers)

