from tkinter import *
from fractions import Fraction

root = Tk()
root.title('find_part_of_amount_in_total_investment')
root.geometry('600x600')


def find_part_of_amount_in_total_investment(val1, val2, val3, val4, val5, val6):
    output = []
    total_investment = float(val1)
    first_stock_rate = float(val2)
    first_stock_market_value = float(val3)
    second_stock_rate = float(val4)
    second_stock_market_value = float(val5)
    total_dividend = float(val6)

    if total_dividend != 0:
        x = ((first_stock_market_value * second_stock_market_value * total_dividend)
             - (second_stock_rate * first_stock_market_value * total_investment)) / \
            ((first_stock_rate * second_stock_market_value) - (second_stock_rate * first_stock_market_value))
        output.append(f'\n1stPart invested on total Amount : {x}')
    else:
        y = (second_stock_rate * total_investment * first_stock_market_value * second_stock_market_value) / \
            ((second_stock_market_value * first_stock_rate * second_stock_market_value) +
             (second_stock_market_value * second_stock_rate * first_stock_market_value))
        output.append(f'\n1stPart invested on total Amount : {y}')
    # output.append(f'\n({val4} / {100}) * (({val1} / {val2}) * {val3}) ')
    return output

def find_better_investment_Stock():
    first_stock_rate = Fraction(input("enter AnnualIncome on 1's share a1 : "))
    first_stock_market_value = float(input("enter Market_value b1 : "))
    second_stock_rate = Fraction(input("enter AnnualIncome on 1's share a2 : "))
    second_stock_market_value = float(input("enter Market_value b2 : "))
    income_tax_rate = float(input("income_tax_rate : "))
    if income_tax_rate == 0:
        x = (first_stock_rate * first_stock_market_value * second_stock_market_value) / first_stock_market_value
        output.append(f'\nannual_income 1st stock : ')
        y = (second_stock_rate * first_stock_market_value * second_stock_market_value) / second_stock_market_value
        output.append(f'\nannual_income 2nd stock : ')
    else:
        x = (first_stock_rate*second_stock_market_value)-((0.01*income_tax_rate)*
                                                          (first_stock_rate*second_stock_market_value))
        output.append(f'\nx_annual_income 1st stock : ')
        y = (second_stock_rate*first_stock_market_value)
        output.append(f'\ny_annual_income 2nd stock : ')
    if x > y:
        print(str(first_stock_rate) + " Stock at " + str(first_stock_market_value) + " is better")
    else:
        print(str(second_stock_rate) + " Stock at " + str(second_stock_market_value) + " is better")


def submit():
    try:
        value = find_part_of_amount_in_total_investment(my_box1.get(), my_box2.get(), my_box3.get(), my_box4.get(),
                                                        my_box5.get(), my_box6.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='total_investment', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='first_stock_rate', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='first_stock_market_value', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='second_stock_rate', font=('Roboto', 10), bg='orange')
my_label4.pack(pady=10)
my_box4 = Entry(root)
my_box4.pack()

my_label5 = Label(root, text='second_stock_market_value', font=('Roboto', 10), bg='orange')
my_label5.pack(pady=10)
my_box5 = Entry(root)
my_box5.pack()

my_label6 = Label(root, text='total_dividend or enter 0', font=('Roboto', 10), bg='orange')
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
