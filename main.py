from tkinter import *
from quiz_input_screen import QuizInputScreen
#Initialize the GUI.
root = Tk()
#Create an instance of QuizInputScreen.
quiz_input_screen = QuizInputScreen()
#Call its widgets() method to load up the interface.
quiz_input_screen.widgets(root)
#Run the tkinter main loop.
root.mainloop()