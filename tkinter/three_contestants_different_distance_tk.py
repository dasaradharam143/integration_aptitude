from tkinter import *

root = Tk()
root.title('three contestants different distance')
root.geometry('600x600')


def three_contestants_different_distance(val1, val2, val3, val4, val5):
    output = []
    a_beat_b = float(val1)
    b_beat_c = float(val2)
    x = float(val3)
    y = x - a_beat_b
    output.append(f'B distance covered = {x}-{a_beat_b}')
    output.append(f'\nB distance covered = {y}')
    b = float(val4)
    z = b - b_beat_c
    output.append(f'\nC distance covered = {b}-{b_beat_c}')
    output.append(f'\nB distance covered = {z}')
    distance = (x / y * b / z)
    output.append(f'\ndistance = {x}/{y}*{b}/{z}')
    output.append(f'\ndistance = {round(distance, 3)}')
    a_beat_c = float(val5)
    a_beat_c = a_beat_c - (a_beat_c / distance)
    output.append(f'\nA_beat_C = {round(a_beat_c, 3)} m ')
    return output


def submit():
    try:
        value = three_contestants_different_distance(my_box1.get(),
                                                     my_box2.get(), my_box3.get(), my_box4.get(), my_box5.get())
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

my_label5 = Label(root, text='A beat C in how much distance', font=('Roboto', 10), bg='orange')
my_label5.pack(pady=10)
my_box5 = Entry(root)
my_box5.pack()

# //////////////////////////////////////////////////////////////////////
# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)

# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
