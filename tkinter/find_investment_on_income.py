from tkinter import *

root = Tk()
root.title('find_investment_on_income')
root.geometry('600x600')


def find_investment_on_income(val1, val2, val3):
    output = []
    income1 = float(val1)
    investment1 = float(val2)
    income2 = float(val3)
    investment2 = float((investment1 * income2) / income1)
    output.append(f'({val2} * {val3}) / {val1}')
    output.append(f'\nInvestment2 or Stock2 : {investment2} ')
    return output


def submit():
    try:
        value = find_investment_on_income(my_box1.get(), my_box2.get(), my_box3.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='Income1 or Earn1 or obtain1', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='Investment1 or Stock1', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='Income2 or Earn2 or obtain2', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

# //////////////////////////////////////////////////////////////////////
# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
