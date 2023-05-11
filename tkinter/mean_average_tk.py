from tkinter import *

root = Tk()
root.title('mean average of numbers')
root.geometry('600x600')


def find_mean_average(val1, val2):
    output=[]
    no_of_denominations = list(map(float, val1.split()))
    avg_of_values = list(map(float, val2.split()))
    total = 0
    total_sum = []
    for i in range(len(no_of_denominations)):
        total += no_of_denominations[i] * avg_of_values[i]
        total_sum.append(total)
    output.append(f'total mean sum = {total_sum}')
    mean = total / sum(no_of_denominations)
    output.append(f'\nmean average = {total} / {sum(no_of_denominations)} = {round(mean, 5)}')
    return output


def submit():
    try:
        value = find_mean_average(my_box.get(), my_box1.get())
        my_label.config(text=' '.join(value))
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
