from tkinter import *

root = Tk()
root.title('average of sum of n powers of numbers')
root.geometry('600x600')

def power_of_n(a, n):
    b = []
    for i in a:
        b.append(i ** n)
    return b


def function1(numbers, power):
    output=[]
    numbers_list = list(map(int, numbers.split()))
    print(numbers_list)
    total = power_of_n(numbers_list, int(power))
    output.append(f'total sum of numbers = {total}')
    avg = sum(total) / len(total)
    output.append(f'\n average of sum of power{power} of numbers = {sum(total)}/{len(total)} = {round(avg, 4)}')
    return output

def submit():
    try:
        value = function1(my_box.get(), my_box1.get())
        my_label.config(text=' '.join(value))
    except:
        my_label.config(text='Enter valid numbers and power')


my_label1 = Label(root, text='enter numbers', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box = Entry(root)
my_box.pack()

my_label2 = Label(root, text='enter power of n', font=('Roboto', 10), bg='orange')
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
