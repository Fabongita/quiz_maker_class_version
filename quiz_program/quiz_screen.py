from tkinter import *
class WidgetsToBeUsed:
    # method for frame
    def frame(self, root):
        self.root = root
        self.intro_frame = Frame(self.root)
        self.start_frame = Frame(self.root)
        self.saved_quizzes_frame = Frame(self.root)
        self.play_frame = Frame(self.root)
        self.button_frame = Frame(self.intro_frame)
        self.button_frame.pack(side="bottom", padx="10")

    # method for saved quizzes button
    def saved_quiz_button(self):
        self.saved_quizzes_button = Button(self.button_frame, text="Saved Quizzes", height="7", width="20",  activebackground="blue", activeforeground="yellow", command=saved_quizzes )
        self.saved_quizzes_button.pack(padx="10", pady="70", side="left")                

    # method for start button
    def starter_button(self):
        self.start_button = Button(self.button_frame, text="Start game", height="7", width="20",  activebackground="blue", activeforeground="yellow", command=start_button_logic )
        self.start_button.pack(padx="10", pady="70", side="left") 

    # method for main menu button
    def menu_button(self):
        self.main_menu_button = Button(self.play_frame, text="Main menu", command=lambda: self.intro_frame.tkraise())
        self.main_menu_button.pack(padx="20", pady="20")

    # method for create quiz button
    def create_quiz_button(self):
        self.quiz_creator_button = Button(self.button_frame, text="Create Quiz", height="7", width="20",  activebackground="blue", activeforeground="yellow", command=quiz_maker )
        self.quiz_creator_button.pack(padx="10", pady="70", side="left") 

    # method for submit button
    def submitter_button(self):
        self.submit_button = Button(self.play_frame, text="Submit", command=submit)
        self.submit_button.pack(pady=10)

    # method for back button
    def back_button(self):
        self.Back_button_saved_quizzes = Button(self.saved_quizzes_frame, text="Back", command=lambda: intro_frame.tkraise())
        self.Back_button_saved_quizzes.pack(padx="20", pady="20", side="right")

    # method for radio buttons
    def radio_buttons(self):
        ...
    
    # method for listbox
    def listbox(self):
        ...

    #method for scrollbar
    def scrollbar(self):
        ...