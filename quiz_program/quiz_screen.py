from tkinter import *
class WidgetsToBeUsed:
    # constructor method
    def __init__(self):
        self.root = None
        self.intro_frame = None
        self.start_frame = None
        self.play_frame = None
        self.saved_quizzes_frame = None
    # method for frame
    def frame(self, root):
        self.root = root
        self.intro_frame = Frame(self.root)
        self.start_frame = Frame(self.root)
        self.saved_quizzes_frame = Frame(self.root)
        self.play_frame = Frame(self.root)

    # method for saved quizzes button
    def saved_quizzes_button(self):
        ...

    # method for start button
    def start_button(self):
        ...

    # method for create quiz button
    def create_quiz_button(self):
        ...
        
    # method for radio buttons
    def radio_buttons(self):
        ...