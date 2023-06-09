from tkinter import *

root = Tk()
root.title('three contestants same distance')
root.geometry('600x600')


def three_contestants_same_distance(val1, val2, val3, val4):
    output = []
    a_beat_b = int(val1)
    b_beat_c = int(val2)
    a = int(val3)
    s = a - a_beat_b
    output.append(f'B covered distance = {a} - {a_beat_b} = {s}')
    b = int(val4)
    c = b - b_beat_c
    output.append(f'\nA covered distance ={b}-{b_beat_c} = {c}')
    distance = (a / s * b / c)
    output.append(f'\ndistance =({a}/{s})*({b}/{c})')
    a_beat_c = a - (a / distance)
    output.append(f'\nA beat C= {a}-{a}/{round(distance, 5)}')
    output.append(f'\nA_beat_C= {round(a_beat_c, 5)} m')
    return output


def submit():
    try:
        value = three_contestants_same_distance(my_box1.get(), my_box2.get(), my_box3.get(), my_box4.get())
        my_label.config(text=' '.join(value))

    except Exception as err:
        my_label.config(text=f'Enter valid numbers\nUnexpected {err=}')


my_label1 = Label(root, text='a_beat_b', font=('Roboto', 10), bg='orange')
my_label1.pack(pady=10)
my_box1 = Entry(root)
my_box1.pack()

my_label2 = Label(root, text='b_beat_c', font=('Roboto', 10), bg='orange')
my_label2.pack(pady=10)
my_box2 = Entry(root)
my_box2.pack()

my_label3 = Label(root, text='Enter Winner distance of A', font=('Roboto', 10), bg='orange')
my_label3.pack(pady=10)
my_box3 = Entry(root)
my_box3.pack()

my_label4 = Label(root, text='Enter Winning distance of b', font=('Roboto', 10), bg='orange')
my_label4.pack(pady=10)
my_box4 = Entry(root)
my_box4.pack()

# //////////////////////////////////////////////////////////////////////
# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
