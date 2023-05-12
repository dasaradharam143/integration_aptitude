from tkinter import *

root = Tk()
root.title('finding x numbers')
root.geometry('600x600')


def finding_x(val1, val2, val3):
    output = []
    total_count = int(val1)
    value = float(val2)
    average = float(val3)
    total = 0
    for i in range(total_count):
        total += value * i
    x = (total_count * average - total) / total_count
    result = []
    for i in range(total_count):
        result.append(x + (value * i))
    output.append(f'the numbers are =  ')
    output.append(f'\n{", ".join(map(str,result))}')
    output.append(f'\nsmallest number = {result[0]}')
    output.append(f'\nlargest number = {result[-1]}')
    return output


def submit():
    try:
        value = finding_x(my_box1.get(), my_box2.get(), my_box3.get())
        my_label.config(text=" ".join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='enter total count of numbers', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='each number increased/decreased by', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='average of total numbers', font=('Roboto', 10), bg='orange')
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
