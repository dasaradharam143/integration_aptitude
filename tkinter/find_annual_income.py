from tkinter import *

root = Tk()
root.title('find_annual_income')
root.geometry('600x600')


def find_annual_income(val1, val2, val3, val4):
    output = []
    total_investment = float(val1)
    investment_in_one_share = float(val2)
    face_value_of_one_share = float(val3)
    dividend = float(val4)
    annual_income = float((dividend / 100) * ((total_investment / investment_in_one_share) * face_value_of_one_share))
    output.append(f'\n({val4} / {100}) * (({val1} / {val2}) * {val3}) ')
    output.append(f'\nAnnual_Income : {annual_income} ')
    return output


def submit():
    try:
        value = find_annual_income(my_box1.get(), my_box2.get(), my_box3.get(), my_box4.get())
        my_label.config(text=' '.join(value))

    except:
        my_label.config(text='Enter valid numbers')


my_label1 = Label(root, text='total_investment', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='investment_in_one_share', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='face_value_of_one_share', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='dividend', font=('Roboto', 10), bg='orange')
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
