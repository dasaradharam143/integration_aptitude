from tkinter import *

root = Tk()
root.title('find_change_in_income_on_service_charge')
root.geometry('600x600')


def find_change_in_income_on_service_charge(val1, val2, val3, val4, val5, val6):
    output = []
    sold_stock_value = float(val1)
    old_stock_rate = float(val2)
    old_stock_value = float(val3)
    new_stock_rate = float(val4)
    new_stock_value = float(val5)
    service_charges = float(val6)
    face_value = 100
    number_of_shares = sold_stock_value / face_value  # no. of shares sold
    output.append(f'\nnumber_of_shares : {number_of_shares}')
    stock_value_purchased = (old_stock_value - (service_charges / 10)) * number_of_shares
    output.append(f'\nstock_value_purchased : {stock_value_purchased}')
    number_of_new_shares_purchased = stock_value_purchased / (new_stock_value + (service_charges / 10))
    output.append(f'\nnumber_of_new_shares_purchased : {number_of_new_shares_purchased}')
    original_income = (sold_stock_value * old_stock_rate) / 100
    output.append(f'\noriginal_income : {original_income}')
    new_income = (new_stock_rate * number_of_new_shares_purchased)
    output.append(f'\nnew_income : {new_income}')
    change_in_income = (new_income - original_income)
    output.append(f'\nchange in Income : {change_in_income}')
    return output


def submit():
    try:
        value = find_change_in_income_on_service_charge(my_box1.get(), my_box2.get(), my_box3.get(), my_box4.get(),
                                                        my_box5.get(), my_box6.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='sold_stock_value', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='old_stock_rate', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='old_stock_value', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='new_stock_rate', font=('Roboto', 10), bg='orange')
my_label4.pack(pady=10)
my_box4 = Entry(root)
my_box4.pack()

my_label5 = Label(root, text='new_stock_value', font=('Roboto', 10), bg='orange')
my_label5.pack(pady=10)
my_box5 = Entry(root)
my_box5.pack()

my_label6 = Label(root, text='service_charges', font=('Roboto', 10), bg='orange')
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
