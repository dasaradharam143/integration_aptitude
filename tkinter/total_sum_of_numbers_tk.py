from tkinter import *

root = Tk()
root.title('total sum of numbers')
root.geometry('600x600')


def sum_of_total_numbers(val1, val2):
    output = []
    average_numbers = float(val1)
    n = float(val2)
    total_sum = average_numbers * n
    output.append(f'total sum of numbers = {total_sum}')
    return output


def submit():
    try:
        value = sum_of_total_numbers(my_box1.get(), my_box2.get())
        my_label.config(text=' '.join(value))
    except:
        my_label.config(text='Enter valid numbers')


my_label1 = Label(root, text='enter average of numbers', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()


my_label2 = Label(root, text='enter number of outcomes', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()


# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
