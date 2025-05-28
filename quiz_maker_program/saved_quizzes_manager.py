from quiz_maker_program.quiz_question import QuizQuestion
import json

class SavedQuizzesManager:
    def __init__(self, file_name = "questions_and_answers.json",):
        self.file_name = file_name

    def add_questions_to_json(self, quiz_builder):
         new_entries = []
         for question in quiz_builder.questions:
            new_entries.append({
                "Quiz name":       question.quiz_name,
                "Questions":       question.question,
                "Options":         question.options,
                "correct answer":  question.correct_answer
            })
         try:
            with open(self.file_name, "r", encoding= "utf-8") as file:
                quizzes = json.load(file)
         except: 
            quizzes = []
         quizzes.extend(new_entries)
        
         with open(self.file_name, "w", encoding= "utf-8") as file:
            json.dump(quizzes, file, indent=2)
