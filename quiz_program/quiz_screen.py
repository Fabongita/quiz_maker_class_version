from tkinter import *
from tkinter import StringVar

class QuizScreen:
    def __init__(self):
        self.root = None
        self.intro_frame = None
        self.start_frame = None
        self.saved_quizzes_frame = None
        self.play_frame = None
        self.button_frame = None
        self.radiobutton_widgets = {}
        self.selected_answer = StringVar()
        self.quiz_questions = StringVar(value="")
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
        self.saved_quizzes_button = Button(self.button_frame, text="Saved Quizzes", height="7", width="20",  activebackground="blue", activeforeground="yellow" )
        self.saved_quizzes_button.pack(padx="10", pady="70", side="left")                

    # method for start button
    def starter_button(self):
        self.start_button = Button(self.button_frame, text="Start game", height="7", width="20",  activebackground="blue", activeforeground="yellow")
        self.start_button.pack(padx="10", pady="70", side="left") 

    # method for main menu button
    def menu_button(self):
        self.main_menu_button = Button(self.play_frame, text="Main menu", command=lambda: self.intro_frame.tkraise())
        self.main_menu_button.pack(padx="20", pady=(10, 5), side="bottom")

    # method for create quiz button
    def create_quiz_button(self):
        self.quiz_creator_button = Button(self.button_frame, text="Create Quiz", height="7", width="20",  activebackground="blue", activeforeground="yellow")
        self.quiz_creator_button.pack(padx="10", pady="70", side="left") 

    # method for submit button
    def submitter_button(self):
        self.submit_button = Button(self.play_frame, text="Submit")
        self.submit_button.pack(pady=(10, 30))

    # method for back button
    def back_button(self):
        self.Back_button_saved_quizzes = Button(self.saved_quizzes_frame, text="Back", command=lambda: self.intro_frame.tkraise())
        self.Back_button_saved_quizzes.pack(padx="20", pady="20", side="right")
    
    #method for the selection button
    def selection_button(self):
        self.select_button = Button(self.start_frame, text="Print Selected")
        self.select_button.pack()

    # method for radio buttons
    def radio_buttons(self):
        self.options_frame = Frame(self.play_frame)
        self.options_frame.pack(padx=20, pady=10, anchor="w")
        self.radiobutton_widgets = {}
        self.selected_answer = StringVar(value="")
        for option_letter in ("a", "b", "c", "d"):
           self.radio_button = Radiobutton(self.options_frame, text=f"\u2022 {option_letter.upper()}",
            variable=self.selected_answer, value=option_letter, indicatoron=True, font=("Courier", 14),
            anchor="w", padx=10, justify="left")
           self.radio_button.pack(fill="x", pady="2", anchor="w")
           self.radiobutton_widgets[option_letter] = self.radio_button
        
    # method for listbox when you press start
    def start_listbox(self):
        self.start_quiz_listbox = Listbox(self.start_frame, font=("Courier", 12)) 
        self.start_quiz_listbox.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)

    #method for scrollbar when you pres start    
    def start_scrollbar(self):
        self.start_quiz_scrollbar = Scrollbar(self.start_frame, orient=VERTICAL, command=self.start_quiz_listbox.yview)
        self.start_quiz_scrollbar.pack(side=RIGHT, fill=Y)

    # method for combining the start scrollbar and listbox
    def start_config(self):
        self.start_quiz_listbox.config(yscrollcommand=self.start_quiz_scrollbar.set)
        self.start_quiz_scrollbar.config(command=self.start_quiz_listbox.yview)

    #method for the scrollbar at the saved quizzes screen
    def saved_quiz_scrollbar(self):
        self.saved_quizzes_scrollbar = Scrollbar(self.saved_quizzes_frame, orient=VERTICAL)
        self.saved_quizzes_scrollbar.pack(side=RIGHT, fill=Y)
    
    # method for the scrollbar at the start button screen
    def saved_quiz_listbox(self):
        self.saved_quizzes_listbox = Listbox(self.saved_quizzes_frame, font=("Courier", 12)) 
        self.saved_quizzes_listbox.pack(side=LEFT, fill=BOTH, expand=True, padx=20, pady=20)
    
    # method for combining the saved quizzes scrollbar and listbox
    def saved_quiz_config(self):
        self.saved_quizzes_listbox.config(yscrollcommand=self.saved_quizzes_scrollbar.set)
        self.saved_quizzes_scrollbar.config(command=self.saved_quizzes_listbox.yview)
    
    #method for the label that displays the question
    def question_label(self):
     self.question_label_widget = Label(self.play_frame, textvariable=self.quiz_questions, font=("Courier", 16), wraplength=500, justify="left")
     self.question_label_widget.pack(pady=20)

    #method for intro label
    def intro_label(self):
        ascii_art = """
________        .__           ________                       
\_____  \  __ __|__|_______  /  _____/_____    _____   ____  
 /  / \  \|  |  \  \___   / /   \  ___\__  \  /     \_/ __ \ 
/   \_/.  \  |  /  |/    /  \    \_\  \/ __ \|  Y Y  \  ___/ 
\_____\ \_/____/|__/_____ \  \______  (____  /__|_|  /\___  >
       \__>              \/         \/     \/      \/     \/ 

"""
        self.introduction_label=Label(self.intro_frame, text=ascii_art, font=("Courier", 12), justify="left")
        self.introduction_label.pack(side="top", padx=20, pady=20)

                