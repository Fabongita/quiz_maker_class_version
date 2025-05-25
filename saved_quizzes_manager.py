from quiz_question import QuizQuestion
import json

class SavedQuizzesManager:
    def __init__(self, file_name = "questions_and_answers.json",):
        self.file_name = file_name

    def add_questions_to_json(self, quiz_builder):
        with open(self.file_name, "r", encoding= "utf-8") as file:
            quizzes = json.load(file)
        quizzes.append(quiz_builder.to_dict())
        with open(self.file_name, "w", encoding= "utf-8") as file:
            json.dump(quizzes, file, indent=2)
