from tkinter import *

root = Tk()
root.title('average of numbers')
root.geometry('600x600')


def average_of_numbers(val1):
    output = []
    numbers = list(map(float, val1.split()))
    n = len(numbers)
    total = sum(numbers)
    average = total / n
    output.append(f'sum of numbers = {total}')
    output.append(f'\naverage of numbers = {total} / {n} = {round(average, 5)}')
    return output


def submit():
    try:
        value = average_of_numbers(my_box.get())
        my_label.config(text=' '.join(value))
    except:
        my_label.config(text='Enter valid numbers')


my_label1 = Label(root, text='enter numbers', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box = Entry(root)
my_box.pack()

# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
