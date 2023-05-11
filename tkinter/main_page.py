from subprocess import call
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Aptitude')
root.geometry('600x600')


def clicked(value):
    if value == 1:
        # root.destroy()
        call(['python', 'find_missing_number_in_mean_average_tk.py'])
    elif value == 2:
        call(['python', 'average_reciprocal_tk.py'])
    elif value == 3:
        call(['python', 'avg_of_sum_of_squares_tk.py'])
    elif value == 4:
        call(['python', 'mean_average_tk.py'])
    elif value == 5:
        call(['python', 'find_missing_number_in_mean_average_tk.py'])
    elif value == 6:
        call(['python', 'find_correct_average_tk.py'])
    elif value == 8:
        call(['python', 'three_contestants_same_distance_tk.py'])


def average():
    v = IntVar()
    Radiobutton(root, text='average', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='reciprocal average', variable=v, value=2, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='avg of sum of squares', variable=v, value=3, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='mean average', variable=v, value=4, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='missing number in mean average', variable=v, value=5,
                command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='correct average', variable=v, value=6, command=lambda: clicked(v.get())).pack()


def races():
    v = IntVar()
    Radiobutton(root, text='races1', variable=v, value=5, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='three contestants same distance', variable=v, value=8,
                command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='races3', variable=v, value=3, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='races4', variable=v, value=4, command=lambda: clicked(v.get())).pack()


def stocks():
    v = IntVar()
    Radiobutton(root, text='Find CostPrice', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find Sold Share_Value', variable=v, value=2, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find Investment on Income', variable=v, value=3, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find Dividend', variable=v, value=4, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find_Annual_Income_/_FV', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find Income on Investment', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find Number_of_shares', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find Total_Debenture', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Interest_on_faceValue', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find_X_Part_in_total_Investment', variable=v, value=1,
                command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find which Stock is Better', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find Loss or gain on amount invested in bank & Stock', variable=v, value=1,
                command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find find_maximum_return', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find find_ratios_of_investments', variable=v, value=1,
                command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find change in Income enter', variable=v, value=1, command=lambda: clicked(v.get())).pack()
    Radiobutton(root, text='Find change in Income on service charge', variable=v, value=1,
                command=lambda: clicked(v.get())).pack()


label = Label(root, text='Aptitude Topics', font=('bold', 18))
label.pack(pady=10)

button1 = Button(root, text='1.Averages', font=('roboto', 10), bg='sky blue', command=average)
button1.pack(pady=8)

button2 = Button(root, text='2.Races and Games', font=('roboto', 10), bg='sky blue', command=races)
button2.pack(pady=8)

button3 = Button(root, text='3.Stocks and Shares', font=('roboto', 10), bg='sky blue', command=stocks)
button3.pack(pady=8)

root.mainloop()
