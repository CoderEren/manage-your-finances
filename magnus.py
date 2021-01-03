from tkinter import *
import tkinter as tk
import sys
import os

window = tk.Tk()
window.title("Magnus - Manage Your Finances")
window.geometry("230x80")

#Functions
def income():
   os.system('python magnus_income.py') 


def expense():
    os.system('python magnus2.py')


#Widgets
income_button = tk.Button(window, text="Income Streams", width=30, command=income)
expense_button = tk.Button(window, text="Expenses", width=30, command=expense)


#Layout
income_button.grid(row=0, column=0, pady=5, padx=5)
expense_button.grid(row=1, column=0, pady=5, padx=5)


window.mainloop()
