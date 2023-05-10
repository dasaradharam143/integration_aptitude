from tkinter import *
from demo import *
root = Tk()
root.title('aptitude')
root.geometry('600x600')

def submit():
    numbers = function1(my_box.get(),my_box1.get())
    mylable.config(text = numbers)


#creating a lable
mylable = Label(root,text='', font=('Roboto',20))
mylable.pack(pady=20)

mylable1 = Label(root,text='enter numbers', font=('Roboto',10)).pack(pady=10)
my_box = Entry(root)
my_box.pack()

mylable2 = Label(root,text='enter power of n', font=('Roboto',10)).pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

#
# my_box2 = Entry(root)
# my_box2.pack()
#
# mylable3 = Label(root,text='', font=('Roboto',20)).pack()
# my_box3 = Entry(root)
# my_box3.pack()

#calling submit function
my_button = Button(root, text="Submit",command=submit)
my_button.pack (pady= 20)




root.mainloop()