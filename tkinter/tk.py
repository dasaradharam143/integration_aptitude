from tkinter import *
from demo import *

root = Tk()
root.title('aptitude')
root.geometry('600x600')


def submit():
    try:
        numbers = function1(my_box.get(), my_box1.get())
        my_label.config(text=numbers)
    except:
        my_label.config(text='enter valid numbers and power')

my_label1 = Label(root, text='enter numbers', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box = Entry(root)
my_box.pack()

my_label2 = Label(root, text='enter power of n', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

#
# my_box2 = Entry(root)
# my_box2.pack()
#
# my_label3 = Label(root,text='', font=('Roboto',20)).pack()
# my_box3 = Entry(root)
# my_box3.pack()

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
