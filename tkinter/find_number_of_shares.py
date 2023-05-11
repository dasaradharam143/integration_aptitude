from tkinter import *

root = Tk()
root.title('find_number_of_shares')
root.geometry('600x600')


def find_number_of_shares(val1, val2, val3):
    output = []
    purchased_total_share_value = float(val1)
    cost_of_each_share = float(val2)
    brokerage = float(val3)
    number_of_share_values = purchased_total_share_value / (
                cost_of_each_share + ((brokerage * cost_of_each_share) / 100))
    output.append(f'\n{val1} / ({val2} + (({val3} * {val2}) / 100)) ')
    output.append(f'\nNumber of ShareValues : {number_of_share_values} ')
    return output


def submit():
    try:
        value = find_number_of_shares(my_box1.get(), my_box2.get(), my_box3.get())
        my_label.config(text=' '.join(value))

    except:
        my_label.config(text='Enter valid numbers')


my_label1 = Label(root, text='purchased_total_share_value', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='cost_of_each_share', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='brokerage', font=('Roboto', 10), bg='orange')
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
