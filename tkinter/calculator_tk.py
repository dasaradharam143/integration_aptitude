from tkinter import *
root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)


def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))


def button_clear():
    e.delete(0, END)


def button_add():
    global f_num
    current1 = e.get()
    f_num = int(current1)
    e.delete(0, END)


def button_equal():
    current2 = e.get()
    e.delete(0, END)
    result = f_num+int(current2)
    e.insert(0, str(result))


myButton_1 = Button(root, text='1', pady=20, padx=40, command=lambda: button_click(1))
myButton_2 = Button(root, text='2', pady=20, padx=40, command=lambda: button_click(2))
myButton_3 = Button(root, text='3', pady=20, padx=40, command=lambda: button_click(3))

myButton_4 = Button(root, text='4', pady=20, padx=40, command=lambda: button_click(4))
myButton_5 = Button(root, text='5', pady=20, padx=40, command=lambda: button_click(5))
myButton_6 = Button(root, text='6', pady=20, padx=40, command=lambda: button_click(6))

myButton_7 = Button(root, text='7', pady=20, padx=40, command=lambda: button_click(7))
myButton_8 = Button(root, text='8', pady=20, padx=40, command=lambda: button_click(8))
myButton_9 = Button(root, text='9', pady=20, padx=40, command=lambda: button_click(9))

myButton_0 = Button(root, text='0', pady=20, padx=40, command=lambda: button_click(0))
myButton_add = Button(root, text='+', pady=20, padx=39, command=lambda: button_add())
myButton_equal = Button(root, text='=', pady=20, padx=91, command=lambda: button_equal())
myButton_clear = Button(root, text='clear', pady=20, padx=82, command=lambda: button_clear())


myButton_1.grid(row=3, column=0)
myButton_2.grid(row=3, column=1)
myButton_3.grid(row=3, column=2)

myButton_4.grid(row=2, column=0)
myButton_5.grid(row=2, column=1)
myButton_6.grid(row=2, column=2)

myButton_7.grid(row=1, column=0)
myButton_8.grid(row=1, column=1)
myButton_9.grid(row=1, column=2)

myButton_0.grid(row=4, column=0)
myButton_clear.grid(row=4, column=1, columnspan=2)
myButton_add.grid(row=5, column=0)
myButton_equal.grid(row=5, column=1, columnspan=2)
root.mainloop()
