import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

root = tk.Tk()
root.title('Aptitude')
root.geometry('600x600')

# label = tk.Label(root, text='')
# label.pack()

button = tk.Button(root, text='button', bg='blue', fg='white')
button.pack()
button.grid(column=3, row=3)
#
r1 = Radiobutton(root, text='average', value=1)
r1.grid(column=1, row=1)
r2 = Radiobutton(root, text='races', value=2)
r2.grid(column=2, row=1)
r3 = Radiobutton(root, text='stocks', value=3)
r3.grid(column=3, row=1)
#
t = Entry(root, width=120)
t.grid(column=3, row=4)
#
#
# def Button1():
#     b = Button(root, text='average file', command=Button1)
#     b.pack()


root.mainloop()
