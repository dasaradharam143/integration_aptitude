from tkinter import *

root = Tk()
root.title('members game')
root.geometry('600x600')


def find_mean_average(val1):
    output = []
    a = list(map(float, val1.split()))
    length = len(a)
    # total = 0
    for i in range(length):
        for j in range(length):
            total = a[j] / 2
            a[j] = round(a[j], 3) / 2
            a[length - i - 1] += round(total, 2)
        output.append(f'\n{", ".join(map(str,a))}')
    output.append(f'\nthe initial amount of each person = {a}')
    return output


def submit():
    try:
        value = find_mean_average(my_box1.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='enter the final amount of each person', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()


# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
