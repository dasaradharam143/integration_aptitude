from tkinter import *

root = Tk()
root.title('mean average of numbers')
root.geometry('600x600')


def find_mean_average(val1, val2):
    no_of_denominations = list(map(float, val1.split()))
    avg_of_values = list(map(float, val2.split()))
    total = 0
    for i in range(len(no_of_denominations)):
        total += no_of_denominations[i] * avg_of_values[i]
    mean = total / sum(no_of_denominations)
    return f'mean average = {total} / {sum(no_of_denominations)} = {round(mean, 5)}'


def submit():
    try:
        value = find_mean_average(my_box.get(), my_box1.get())
        my_label.config(text=value)
    except:
        my_label.config(text='Enter valid numbers')


my_label1 = Label(root, text='enter denominations', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box = Entry(root)
my_box.pack()

my_label2 = Label(root, text='enter values', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
