from tkinter import *

root = Tk()
root.title('find_maximum_return')
root.geometry('600x600')


def find_maximum_return(val1, val2, val3, val4):
    output = []
    investing_amount = float(val1)
    comparative_percentage_condition = float(val2)
    annual_return_percent_on_bond_a = float(val3)
    annual_return_percent_on_bond_b = float(val4)
    investment_in_bond_a = 100 * investing_amount / (comparative_percentage_condition + 100)
    investment_in_bond_b = investing_amount - investment_in_bond_a
    output.append(f'\ninvestment in bond a : {investment_in_bond_a} \ninvestment in bond b : {investment_in_bond_b}')
    maximum_return = (annual_return_percent_on_bond_a * investment_in_bond_a / 100) + \
                     (annual_return_percent_on_bond_b * investment_in_bond_b / 100)
    output.append(f'\nMaximum Return : {maximum_return}')

    return output


def submit():
    try:
        value = find_maximum_return(my_box1.get(), my_box2.get(), my_box3.get(), my_box4.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='investing_amount', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='comparative_percentage_condition', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='annual_return_percent_on_bond_a', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='annual_return_percent_on_bond_b', font=('Roboto', 10), bg='orange')
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
