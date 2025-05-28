import sys
import os
from tkinter import Tk
from quiz_screen import QuizScreen
from button_logic import ButtonLogic

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

#add main function that sets up and runs the quiz GUI app 
def main():
    # create main window
    root = Tk()
    root.title("Quiz Program")
    root.geometry("800x600")

    # initialize UI handler
    ui = QuizScreen()
    ui.frame(root)

    # build GUI widgets
    ui.radio_buttons()
    ui.start_listbox()
    ui.start_scrollbar()
    ui.start_config()
    ui.saved_quiz_listbox()
    ui.saved_quiz_scrollbar()
    ui.saved_quiz_config()
    ui.question_label()

    ui.starter_button()
    ui.saved_quiz_button()
    ui.create_quiz_button()
    ui.menu_button()
    ui.submitter_button()
    ui.back_button()
    ui.selection_button()

    # connect UI with logic
    logic = ButtonLogic(ui=ui)

    # configure button commands
    ui.start_button.config(command=logic.start_button_logic)
    ui.quiz_creator_button.config(command=logic.create_quiz)
    ui.saved_quizzes_button.config(command=logic.saved_quizzes)
    ui.select_button.config(command=logic.load_button)
    ui.submit_button.config(command=logic.submit)

    # raise intro frame
    ui.intro_frame.tkraise()

    # start GUI event loop
    root.mainloop()

if __name__ == "__main__":
    main()
    