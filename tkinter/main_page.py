from subprocess import call
import tkinter as tk
from tkinter import *


root = tk.Tk()
root.title('Aptitude')
root.geometry('600x600')

def average():
    return call(['python','tk.py'])


label = Label(root, text='Aptitude Topics', font=('bold', 18))
label.pack(pady=10)

button1 = Button(root, text='1.Averages', font=('roboto', 10), bg='sky blue',command=average)
button1.pack(pady=8)

button2 = Button(root, text='2.Races and Games', font=('roboto', 10), bg='sky blue')
button2.pack(pady=8)

button3 = Button(root, text='3.Stocks and Shares', font=('roboto', 10), bg='sky blue')
button3.pack(pady=8)

root.mainloop()
