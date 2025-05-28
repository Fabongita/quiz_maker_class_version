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
        for frame in (self.intro_frame, self.saved_quizzes_frame, self.start_frame, self.play_frame):
            frame.place(relwidth=1, relheight=1)

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
    
    #method for the selection button
    def selection_button(self):
        self.select_button = Button(self.start_frame, text="Print Selected", command=load_button)
        self.select_button.pack()

    # method for radio buttons
    def radio_buttons(self):
        self.radiobutton_widgets = {}
        self.selected_answer = StringVar(value="")
        self.options_frame = Frame(self.play_frame)
        self.options_frame.pack(anchor="w", padx=20, pady=10)
        for option_letter in ("a", "b", "c", "d"):
           self.radio_button = Radiobutton(self.options_frame, text=f"\u2022 {option_letter.upper()}",
            variable=selected_answer, value=option_letter, indicatoron=True, font=("Courier", 14),
            anchor="w", padx=10)
           self.radio_button.pack(fill="x", pady="2")
           self.radiobutton_widgets[option_letter] = self.radio_button
        
    # method for listbox
    def listbox(self):
        self.start_quiz_listbox = Listbox(self.start_frame, font=("Courier", 12)) 
        self.start_quiz_listbox.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)

    #method for the scrollbar at the saved quizzes screen
    def saved_quiz_scrollbar(self):
        self.saved_quizzes_scrollbar = Scrollbar(self.saved_quizzes_frame, orient=VERTICAL, command=quiz_listbox.yview)
        self.saved_quizzes_scrollbar.pack(side=RIGHT, fill=Y)
    
