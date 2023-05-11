from tkinter import *

root = Tk()
root.title('find_total_investment_on_debenture')
root.geometry('600x600')


def find_total_investment_on_debenture(val1, val2, val3, val4, val5):
    output = []
    total_income = float(val1)
    debenture_percentage = float(val2)
    face_value = float(val3)
    cost_of_each_debenture = float(val4)
    brokerage = float(val5)
    one_share_income = (debenture_percentage * face_value) / 100
    number_of_debenture = float(total_income / one_share_income)
    cost_of_each_debenture_after_brokerage = float(cost_of_each_debenture +
                                                   ((brokerage * cost_of_each_debenture) / 100))
    total_investment_on_debentures = float(cost_of_each_debenture_after_brokerage * number_of_debenture)
    output.append(f'\none_share_income : ({val2} * {val3}) / 100 ')
    output.append(f'\nnumber_of_debenture : {val1}/{one_share_income}')
    output.append(f'\ncost_of_each_debenture_after_brokerage : {val4} + (({val5} * {val4})/100)')
    output.append(f'\n{cost_of_each_debenture_after_brokerage} * {number_of_debenture} ')
    output.append(f'\nTotal Investment on Debentures : {total_investment_on_debentures} ')
    return output


def submit():
    try:
        value = find_total_investment_on_debenture(my_box1.get(), my_box2.get(), my_box3.get(), my_box4.get(),
                                                   my_box5.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='total_income', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='debenture_percentage', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='face_value', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='cost_of_each_debenture', font=('Roboto', 10), bg='orange')
my_label4.pack(pady=10)
my_box4 = Entry(root)
my_box4.pack()

my_label5 = Label(root, text='brokerage', font=('Roboto', 10), bg='orange')
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
