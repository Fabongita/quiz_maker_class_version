class QuizQuestion:
    def __init__(self, quiz_name, question, correct_answer, options):
        self.quiz_name = quiz_name
        self.question = question
        self.correct_answer = correct_answer
        self.options = options
    def turn_to_dict(self):
        return {"quiz name":self.quiz_name,
                "question": self.question,
                "correct answer": self.correct_answer,
                "options": self.options}
        