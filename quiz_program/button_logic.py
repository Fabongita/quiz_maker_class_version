from quiz_screen import QuizScreen
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
        


