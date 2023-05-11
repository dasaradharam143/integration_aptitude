from tkinter import *

root = Tk()
root.title('missing number from average')
root.geometry('600x600')


def missing_numbers(val1, val2):
    output = []
    numbers = list(map(float, val1.split()))
    average = float(val2)
    n = len(numbers) + 1
    total = sum(numbers)
    missing_number = (average * n) - total
    output.append(f'sum of numbers = {total} \nsum of total numbers = {average * n}')
    output.append(f'\nmissing number = {average * n} -{total} = {missing_number}')
    return output


def submit():
    try:
        value = missing_numbers(my_box1.get(), my_box2.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='enter the numbers', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()


my_label2 = Label(root, text='enter the average of total numbers', font=('Roboto', 10), bg='orange')
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
