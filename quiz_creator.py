# Import tkinker for the user interface  
from tkinter import *
from tkinter import ttk, simpledialog  #added simple dialogue for simple user interaction
# Import random to make sure that the correct answer is at least randomly in a b c or d
import random
import json 

# add class for the whole quiz creator
class QuizCreatorScreen:
    def __init__(self):
        def questions_options_answers():
    root.withdraw() # closes the main window to ensure that the user gets to type freely without having to manually click to type
    quiz_name = simpledialog.askstring("input name of the quiz", "Input the name of the quiz") #ask user to add quiz name
    while flow_of_the_game:
        option_label = ["a", "b", "c", "d"] #initializes the choices a b c and d which resets after the loop starts again
        question = simpledialog.askstring("input question", "Think of a multiple choice question and input it here (enter nothing if you are done): ") # asks users to add there question, and add blank if they want to stop
        
        if not question: #checks if the input in the question variable is a blank space or not
         # Read the file 
         file_name = "questions_and_answers.json"
         with open(file_name, "r", encoding= "utf-8") as file:
            contents = json.load(file)
         # extend it to the question list to that it doesn't overwrite
         contents.extend(question_list)

            #add a file handling logic that collects the data from the questions list to a text file
         with open(file_name, "w", encoding= "utf-8") as file:
            json.dump(contents, file, indent=4) 
            root.destroy()
            break #breaks the whole loop
        
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
        
        random.shuffle(option_label) #shuffles the options list
        
        correct_label = option_label[0] #takes only one option from the list
        
        correct_option = {correct_label: correct_answer} #assigns the correct answer to the label
        
        incorrect_option = {}
        
        for index, label in enumerate(option_label[1:]): # goes through the randomized option labels and assigns the index and the specific label
            incorrect_option[label] = wrong_answers[index]
        
        all_options = {**correct_option, **incorrect_option} # merges all the options

        # add a dictionary that reorders the options dictionary so that it is in order: a, b, c, d
        ordered_options = {}

        for label in ["a", "b", "c", "d"]:
           if label in all_options:
                ordered_options[label] = all_options[label]

        question_data = {"Quiz name": quiz_name, 
                         "Questions": question,
                        "Options": ordered_options,
                        "correct answer": correct_label}
    
        question_list.append(question_data)