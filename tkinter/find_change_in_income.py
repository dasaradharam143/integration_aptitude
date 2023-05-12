from tkinter import *

root = Tk()
root.title('find_change_in_income')
root.geometry('600x600')


def find_change_in_income(val1, val2, val3, val4, val5, val6):
    output = []
    investment = float(val1)
    dividend_percentage_of_first_stock_value = float(val2)
    first_stock_value = float(val3)
    sold_one_stock = float(val4)
    new_stock_value_dividend_percentage = float(val5)
    new_stock_value_invested = float(val6)
    number_of_shares = (investment / first_stock_value)
    original_income = dividend_percentage_of_first_stock_value * number_of_shares
    output.append(f'\noriginal_income : {original_income}')
    new_income = (sold_one_stock * number_of_shares * new_stock_value_dividend_percentage) / new_stock_value_invested
    output.append(f'\nnew_income : {new_income}')
    change_in_income = (new_income - original_income)
    output.append(f'\nchange in Income : {change_in_income}')

    return output


def submit():
    try:
        value = find_change_in_income(my_box1.get(), my_box2.get(), my_box3.get(), my_box4.get(),
                                      my_box5.get(), my_box6.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='investment', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='dividend_percentage_of_first_stock_value', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='first_stock_value', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='sold_one_stock', font=('Roboto', 10), bg='orange')
my_label4.pack(pady=10)
my_box4 = Entry(root)
my_box4.pack()

my_label5 = Label(root, text='new_stock_value_dividend_percentage', font=('Roboto', 10), bg='orange')
my_label5.pack(pady=10)
my_box5 = Entry(root)
my_box5.pack()

my_label6 = Label(root, text='new_stock_value_invested', font=('Roboto', 10), bg='orange')
my_label6.pack(pady=10)
my_box6 = Entry(root)
my_box6.pack()

# //////////////////////////////////////////////////////////////////////
# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
