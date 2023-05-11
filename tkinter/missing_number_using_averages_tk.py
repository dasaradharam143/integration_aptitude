from tkinter import *

root = Tk()
root.title('missing number using averages')
root.geometry('600x600')


def missing_numbers_case1(val1, val2, val3):
    output = []
    total_average = float(val1)
    average_numbers = float(val2)
    total_numbers = int(val3)
    sum_of_numbers = average_numbers * (total_numbers - 1)
    missing_number = total_numbers * total_average - sum_of_numbers
    output.append(f'sum of numbers = {sum_of_numbers} \nsum of total numbers = {total_numbers * total_average}')
    output.append(f'\nmissing number = {missing_number}')
    return output


def submit():
    try:
        value = missing_numbers_case1(my_box1.get(), my_box2.get(), my_box3.get())
        my_label.config(text=' '.join(value))
    except:
        my_label.config(text='Enter valid numbers')


my_label1 = Label(root, text='enter the average of total numbers', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()


my_label2 = Label(root, text='enter the average of numbers', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()


my_label3 = Label(root, text='total no of outcomes', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
