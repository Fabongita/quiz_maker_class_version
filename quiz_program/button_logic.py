from quiz_screen import QuizScreen
from quiz_maker_program import launch_quiz_maker
import json
from tkinter import *

class ButtonLogic:
    def __init__(self, ui, current_questions = None, current_index = 0, score = 0):
        if current_questions is None:
            current_questions = []
        self.ui = ui
        self.current_questions = current_questions
        self.current_index = current_index
        self.score = score
    
    # method for when the start button is pressed
    def start(self, questions):
        self.current_questions = questions
        self.current_index = 0
        self.score = 0
        
        self.show_question()
        
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
                self.show_question()
        else:
                self.ui.quiz_questions.set(f"Quiz complete! You scored {self.score} out of {len(self.current_questions)}.")
                for radiobutton in self.ui.radiobutton_widgets.values():
                    radiobutton.pack_forget()
                self.ui.submit_button.pack_forget()
                self.ui.main_menu_button.pack()
    
    #method for showing the current question and current options
    def show_question(self):     
        self.question_data = self.current_questions[self.current_index]
        self.ui.quiz_questions.set(self.question_data["Questions"])
        self.ui.selected_answer.set("")
        self.options = self.question_data["Options"]
        for letter, widget in self.ui.radiobutton_widgets.items():
            widget.config(text=f"{letter.upper()}: {self.options[letter]}")
    
    # method for creating a quiz when the button is pressed
    def create_quiz(self):
         launch_quiz_maker()
    
    # method for loading the button
    def load_button(self):
         self.selected = self.ui.start_quiz_listbox.curselection()
         if not self.selected:
          return  #returns nothing if nothing is selected
         else:
          self.index = self.selected[0] 
         self.quiz_name = self.ui.start_quiz_listbox.get(self.index)
         with open("questions_and_answers.json", "r", encoding= "utf-8" ) as file:
          contents = json.load(file)
         self.questions_to_play = [question for question in contents if question["Quiz name"] == self.quiz_name]
         self.start(self.questions_to_play)  
    # Method for the when the start is pressed that the start button is going to use
    def start_button_logic(self):
        with open("questions_and_answers.json", "r", encoding= "utf-8" ) as file:
            json_file = json.load(file)
        self.all_names = [entry["Quiz name"] for entry in json_file]
        self.unique_name = sorted(set(self.all_names))
        self.ui.start_quiz_listbox.delete(0, END)
    
        for entry in self.unique_name:
          self.ui.start_quiz_listbox.insert(END, entry)
        self.ui.start_frame.tkraise()   
    # method for the saved quizzes the quiz saved quizzes button is going to use
    def saved_quizzes(self):
         with open("questions_and_answers.json", "r", encoding= "utf-8" ) as file:
            json_file = json.load(file)

         # Get the unique quiz names
         self.all_names = [entry["Quiz name"] for entry in json_file]
         self.unique_name = list(set(self.all_names))
    
         # Populate the Listbox with quiz names
         self.ui.saved_quizzes_listbox.delete(0, END)
    
         for entry in self.unique_name:
             self.ui.saved_quizzes_listbox.insert(END, entry)
         self.ui.saved_quizzes_frame.tkraise()