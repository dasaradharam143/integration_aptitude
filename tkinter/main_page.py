from subprocess import call
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Aptitude')
root.geometry('600x600')


def clicked(value):
    # mylabel = Label(root,text=value)
    # mylabel.pack()
    if value == 1:
        root.destroy()
        call(['python', 'find_average.py'])
    else:
        call(['python', 'get_name.py'])
def average():
    # return call(['python', 'find_average.py'])

    v=IntVar()
    Radiobutton(root, text='find average',variable=v, value=1,command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='reciprocal average',variable=v, value=2,command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='avg of sum of squares',variable=v, value=3,command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='mean average.py',variable=v, value=4,command=lambda: clicked(v.get())).pack()

def races():
    # return call(['python', 'find_average.py'])

    v=IntVar()
    Radiobutton(root, text='races1',variable=v, value=1,command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='races2',variable=v, value=2,command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='races3',variable=v, value=3,command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='races4',variable=v, value=4,command=lambda: clicked(v.get())).pack()

def stocks():
    # return call(['python', 'find_average.py'])

    v=IntVar()
    Radiobutton(root, text='stocks1',variable=v, value=1,command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='stocks2',variable=v, value=2,command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='stocks3',variable=v, value=3,command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='stocks4',variable=v, value=4,command=lambda: clicked(v.get())).pack()



label = Label(root, text='Aptitude Topics', font=('bold', 18))
label.pack(pady=10)

button1 = Button(root, text='1.Averages', font=('roboto', 10), bg='sky blue', command=average)
button1.pack(pady=8)

button2 = Button(root, text='2.Races and Games', font=('roboto', 10), bg='sky blue', command=races)
button2.pack(pady=8)

button3 = Button(root, text='3.Stocks and Shares', font=('roboto', 10), bg='sky blue',command=stocks)
button3.pack(pady=8)

root.mainloop()
