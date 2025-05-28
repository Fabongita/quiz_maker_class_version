from quiz_screen import QuizScreen
from quiz_maker_program import launch_quiz_maker

class ButtonLogic:
    def __init__(self, current_questions = [], current_index = 0, score = 0, ui):
        self.ui = ui
        self.current_questions = current_questions
        self.current_index = current_index
        self.score = score
    
    # method for when the start button is pressed
    def start(self, questions):
        self.current_questions = questions
        self.current_index = 0
        self.score = 0
        
        self.ui.show_questions()
        
        self.ui.main_menu_button.pack_forget()    
        
        for widget in self.ui.radiobutton_widgets.values():
            widget.pack(fill="x", pady="2")
        self.ui.submit_button.pack(pady=10)
        self.ui.play_frame.tkraise()

    # method for when the submit button is pressed
    def submit(self):
        self.choice = self.ui.selected_answer.get()
        self.correct = self.current_questions[self.current_index]["correct answer"]
        if self.choice == self.correct:
            self.score += 1
        self.current_index += 1
        if self.current_index < len(self.current_questions):
                self.ui.show_question()
        else:
                self.ui.quiz_questions.set(f"Quiz complete! You scored {self.score} out of {len(self.current_questions)}.")
                for radiobutton in self.ui.radiobutton_widgets.values():
                    radiobutton.pack_forget()
                self.ui.submit_button.pack_forget()
                self.ui.main_menu_button.pack()
    
    #method for showing the current question and current options
    def show(self):     
        self.question_data = self.current_questions[self.current_index]
        self.ui.quiz_questions.set(self.question_data["Questions"])
        self.ui.selected_answer.set("")
        self.options = self.question_data["Options"]
        for letter, widget in self.ui.radiobutton_widgets.items():
            widget.config(text=f"{letter.upper()}: {self.options[letter]}")
    
    # method for creating a quiz when the button is pressed
    def create_quiz(self):
         launch_quiz_maker()