from tkinter import *

root = Tk()
root.title('average of sum of n powers of numbers')
root.geometry('600x600')


def function1(numbers_list):
    output = []
    numbers = list(map(float, numbers_list.split()))
    b = []
    for i in numbers:
        b.append(round(1 / i, 5))
    output.append('reciprocals of numbers = ' + str(b))
    total = round(sum(b), 5)
    output.append(f'\nsum of numbers {total}')
    avg = sum(b) / len(b)
    output.append(f'\naverage of numbers {total}/{len(b)} = {round(avg, 5)}')
    return output


def submit():
    try:
        value = function1(my_box.get())
        my_label.config(text=' '.join(value))
    except:
        my_label.config(text='Enter valid numbers')


my_label1 = Label(root, text='enter numbers in denominators', font=('Roboto', 10), bg='orange')
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
