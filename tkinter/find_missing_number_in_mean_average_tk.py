from tkinter import *

root = Tk()
root.title('find missing number in mean average')
root.geometry('600x600')


def find_missing_number(val1, val2, val3):
    output = []
    no_of_denominations = list(map(float, val1.split()))
    avg_of_values = list(map(float, val2.split()))
    index_0 = avg_of_values.index(0)
    average = int(val3)
    total = 0
    for i in range(len(no_of_denominations)):
        total += no_of_denominations[i] * avg_of_values[i]
    missing_number = (average * sum(no_of_denominations) - total) / no_of_denominations[index_0]
    output.append(f'missing number = {round(missing_number, 4)}')
    return output


def submit():
    try:
        value = find_missing_number(my_box1.get(), my_box2.get(), my_box3.get())
        my_label.config(text=' '.join(value))

    except:
        my_label.config(text='Enter valid numbers')


my_label1 = Label(root, text='enter denominations', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='enter values (enter 0 inplace of "missing number")', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='enter average', font=('Roboto', 10), bg='orange')
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
