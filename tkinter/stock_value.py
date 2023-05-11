from tkinter import *

root = Tk()
root.title('find_stock_value on selling_price')
root.geometry('600x600')


def find_stock_value(val1, val2):
    output = []
    selling_price = int(val1)
    brokerage = int(val2)
    stock_value = float(selling_price - brokerage)
    output.append(f'{val1}-{val2}')
    output.append(f'\nstock_value : {stock_value} ')
    return output


def submit():
    try:
        value = find_stock_value(my_box1.get(), my_box2.get())
        my_label.config(text=' '.join(value))
    except:
        my_label.config(text='Enter valid numbers')


my_label1 = Label(root, text='selling_price', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='brokerage', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

# //////////////////////////////////////////////////////////////////////
# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
