from tkinter import *
from fractions import Fraction

root = Tk()
root.title('find_loss_or_gain_on_amount_invested_in_bank_and_stock')
root.geometry('600x600')


def find_loss_or_gain_on_amount_invested_in_bank_and_Stock(val1, val2, val3, val4, val5):
    output = []
    total_investment = Fraction(val1)
    bank_interest = float(val2)
    face_value = Fraction(val3)
    one_share_value = float(val4)
    dividend = float(val5)
    bank_income = float((total_investment * bank_interest) / 100)
    stock_income = float(((dividend * face_value) / 100) * (total_investment / one_share_value))
    output.append(f'\nbank_income : {bank_income} ')
    output.append(f'\nTotal Income on Stock : {stock_income} ')
    if bank_income > stock_income:
        difference_in_income = float(bank_income - stock_income)
        output.append(f'\nLOSS : {difference_in_income}')
    else:
        difference_in_income = float(stock_income - bank_income)
        output.append(f'\nGAIN : {difference_in_income}')
    return output


def submit():
    try:
        value = find_loss_or_gain_on_amount_invested_in_bank_and_Stock(my_box1.get(), my_box2.get(), my_box3.get(),
                                                                       my_box4.get(), my_box5.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='total_investment', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='bank_interest', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='face_value', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='one_share_value', font=('Roboto', 10), bg='orange')
my_label4.pack(pady=10)
my_box4 = Entry(root)
my_box4.pack()

my_label5 = Label(root, text='dividend', font=('Roboto', 10), bg='orange')
my_label5.pack(pady=10)
my_box5 = Entry(root)
my_box5.pack()

# //////////////////////////////////////////////////////////////////////
# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
