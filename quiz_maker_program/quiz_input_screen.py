from .quiz_builder import QuizBuilder
from tkinter import *
from tkinter import simpledialog
from .saved_quizzes_manager import SavedQuizzesManager

class QuizInputScreen:
    def __init__(self, png_pic = "quiz_maker_pic.png", ):
       self.picture = png_pic
       self.quiz_builder = None
       self.root = None
    def ask_strings(self):
       self.root.withdraw()
       quiz_name = simpledialog.askstring("input name of the quiz", "Input the name of the quiz") #ask user to add quiz name
       self.quiz_builder = QuizBuilder(quiz_name)
       while True:
         question = simpledialog.askstring("input question", "Think of a multiple choice question and input it here (enter nothing if you are done): ") # asks users to add there question, and add blank if they want to stop
         if not question:
            break
         correct_answer = simpledialog.askstring("Input correct answer", "input the correct answer: ") #ask user to input the correct answer    
         wrong_answers = []
         #create a for loop that repeats the askstring function 3 times
         for i in range(3):
            simple_dialogue_answer = simpledialog.askstring("3 incorrect answers input ", f"Please input the wrong answer 3 times ({i+1} times inputted): ")
            if simple_dialogue_answer is None: # checks if the answer is blank
               simple_dialogue_answer = "" #converts the blank into space
            wrong_answers.append(simple_dialogue_answer) #appends the answers into the wrong answer list

         if len(wrong_answers) != 3: # checks if the wrong answers are not exactly 3
            print("Please input exactly 3 answers")
            return 
         self.quiz_builder.add_question(correct_answer, wrong_answers, question)
       manager = SavedQuizzesManager()
       manager.add_questions_to_json(self.quiz_builder)

    def widgets(self, root):
      self.root = root
      self.logo = PhotoImage(file= self.picture)
      logo_label = Label(root, image = self.logo)
      logo_label.pack(pady=10)
      # start button        
      button = Button(root, text="Press if you want to start adding questions", command= self.ask_strings)
      button.pack(pady=40)
       