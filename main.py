# Import modules
import pygame
from tkinter import *

def type(x):
    pass

# Create calculating functions
def addition(*x):
    pass

def subtraction(*x):
    pass

def multiplication(*x):
    pass

def division(*x):
    pass


# Create GUI
root = Tk()
root.title("Calculator")

b1 = Button(root,text='1').grid(column=1,row=1,padx=2,pady=5)
b2 = Button(root,text='2').grid(column=2,row=1,padx=2,pady=5)
b3 = Button(root,text='3').grid(column=3,row=1,padx=2,pady=5)
b4 = Button(root,text='4').grid(column=1,row=2,padx=2,pady=5)
b5 = Button(root,text='5').grid(column=2,row=2,padx=2,pady=5)
b6 = Button(root,text='6').grid(column=3,row=2,padx=2,pady=5)
b7 = Button(root,text='7').grid(column=1,row=3,padx=2,pady=5)
b8 = Button(root,text='8').grid(column=2,row=3,padx=2,pady=5)
b9 = Button(root,text='9').grid(column=3,row=3,padx=2,pady=5)

b_add = Button(root,text='+').grid(column=4,row=1,padx=2,pady=5)
b_minus = Button(root,text='-').grid(column=5,row=1,padx=2,pady=5)
b_multiply = Button(root,text='x').grid(column=4,row=2,padx=2,pady=5)
b_divide = Button(root,text='÷').grid(column=5,row=2,padx=2,pady=5)

b_pi = Button(root,text='π').grid(column=4,row=3,padx=2,pady=5)
b_ans = Button(root,text='=').grid(column=5,row=3,padx=2,pady=5)


root.mainloop()
