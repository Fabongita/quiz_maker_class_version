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
        options = dict(zip(option_label, all_answers))
        correct_label = next(label for label, answer in options.items() if answer == correct_answer)
        quiz_question = QuizQuestion(
        quiz_name=self.quiz_name,
        question=question,
        correct_answer=correct_label,
        options=options
    )
        self.questions.append(quiz_question)
    def to_dictionary(self):
        return { 
            "quiz name" : self.quiz_name,
            "questions" : [question.turn_to_dict() for question in self.questions]
        }

    