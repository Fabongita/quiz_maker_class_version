class ButtonLogic:
    def __init__(self, current_questions = [], current_index = 0, score = 0):
        self.current_questions = current_questions
        self.current_index = current_index
        self.score = score
    def start(questions):
        global current_questions, current_index, score
        current_questions = questions
        current_index = 0
        score = 0
        
        show_question() 
        
        main_menu_button.pack_forget()    
        
        for widget in radiobutton_widgets.values():
            widget.pack(fill="x", pady="2")
        submit_button.pack(pady=10)
        play_frame.tkraise()

