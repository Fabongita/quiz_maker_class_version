from quiz_question import QuizQuestion
import json

class SavedQuizzesManager:
    def __init__(self, file_name = "questions_and_answers.json",):
        self.file_name = file_name

    def add_questions_to_json(self):
        with open(self.file_name, "r", encoding= "utf-8") as file:
            contents = json.load(file)
        contents.extend()