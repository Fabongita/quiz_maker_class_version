import tkinter as tk
from quiz_maker_program.quiz_input_screen import QuizInputScreen
from quiz_maker_program.saved_quizzes_manager import SavedQuizzesManager

class MainScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Quiz Maker")
        self.root.geometry("800x600")
        screen = QuizInputScreen()
        screen.widgets(self.root)

    def run(self):
        self.root.mainloop()

def launch_quiz_maker():
    """Call this to pop up the quiz‐maker GUI."""
    app = MainScreen()
    app.run()

if __name__ == "__main__":
    launch_quiz_maker()
