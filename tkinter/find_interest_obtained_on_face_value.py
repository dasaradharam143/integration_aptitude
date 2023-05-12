from tkinter import *
from fractions import Fraction

root = Tk()
root.title(' find_interest_obtained_on_faceValue')
root.geometry('600x600')


def find_interest_obtained_on_face_value(val1, val2, val3, val4):
    output = []
    number_of_shares = float(val1)
    each_share_value = float(val2)
    discount = float(val3)
    dividend_percentage = Fraction(val4)
    investment = float(number_of_shares * (each_share_value - discount))
    face_value = float(number_of_shares * each_share_value)
    dividend = Fraction((dividend_percentage / 100) * face_value)
    interest_obtained = float(dividend * 100) / investment

    # output.append(f'\n({val4} / {100}) * (({val1} / {val2}) * {val3}) ')
    output.append(f'\ninterest_obtained : {interest_obtained} %')
    return output


def submit():
    try:
        value = find_interest_obtained_on_face_value(my_box1.get(), my_box2.get(), my_box3.get(), my_box4.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='number_of_shares', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='each_share_value', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='discount', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='dividend_percentage', font=('Roboto', 10), bg='orange')
my_label4.pack(pady=10)
my_box4 = Entry(root)
my_box4.pack()

# //////////////////////////////////////////////////////////////////////
# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
