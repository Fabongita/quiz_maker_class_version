from quiz_question import QuizQuestion

class QuizBuilder():
    def __init__(self, quiz_name):
        self.quiz_name = quiz_name
        self.questions = []
        