from tkinter import *

root = Tk()
root.title('find correct average')
root.geometry('600x600')


def function1(val1, val2, val3, val4):
    output = []
    average_numbers = float(val1)
    n = int(val2)
    total_sum = average_numbers * n
    incorrect = list(map(float, val3.split()))
    correct = list(map(float, val4.split()))
    correct_total = total_sum - sum(incorrect) + sum(correct)
    correct_average = correct_total / n
    output.append(f'correct total = {total_sum} - {sum(incorrect)}+ {sum(correct)} = {correct_total}')
    output.append(f'\ncorrect average = {correct_total} / {n} = {round(correct_average, 2)}')
    return output


def submit():
    try:
        value = function1(my_box1.get(), my_box2.get(), my_box3.get(), my_box4.get())
        my_label.config(text=' '.join(value))
    except:
        my_label.config(text='Enter valid numbers and power')


my_label1 = Label(root, text='enter average of numbers', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='enter number of outcomes', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='incorrect values', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='correct values', font=('Roboto', 10), bg='orange')
my_label4.pack(pady=10)
my_box4 = Entry(root)
my_box4.pack()

# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)


# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
