
from tkinter import Toplevel, Tk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from quiz_maker_program.quiz_input_screen import QuizInputScreen
from quiz_maker_program.saved_quizzes_manager import SavedQuizzesManager

class MainScreen:
    def __init__(self, parent):
        self.parent = parent
        self.root = Toplevel(parent)
        self.root.title("Quiz Maker")
        self.root.geometry("800x600")
        self.root.transient(parent)    # this will keep it on top of parent
        self.root.grab_set()           # block interaction with parent
        self.root.focus()
        screen = QuizInputScreen()
        screen.widgets(self.root)

    def run(self):
        # wait until the Toplevel is destroyed
        self.root.wait_window()

def launch_quiz_maker(parent):
    """Call this to pop up the quiz‐maker GUI."""
    app = MainScreen(parent)
    app.run()

if __name__ == "__main__":
    root = Tk()
    root.after(0, lambda: launch_quiz_maker(root))
    root.mainloop()


