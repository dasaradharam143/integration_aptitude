from tkinter import *

root = Tk()
root.title('three contestants same distance')
root.geometry('600x600')


def three_contestants_same_distance(val1,val2,val3,val4):
    output=[]
    a_beat_b = int(val1)
    b_beat_c = int(val2)
    a = int(val3)
    b = a - a_beat_b
    output.append(f'B covered distance = {a} - {a_beat_b} = {b}')
    B = int(val4)
    c = B - b_beat_c
    output.append(f'\nA covered distance ={B}-{b_beat_c} = {c}')
    distance = (a / b * B / c)
    output.append(f'distance ={a}/{b}*{B}/{c}')
    a_beat_c = a - (a / distance)
    output.append(f'\nA beat C= {a}-{a}/{distance}')
    output.append("\nA_beat_C=" + str(a_beat_c) + 'm')
    return output
def submit():
    try:
        value = three_contestants_same_distance(my_box1.get(),my_box2.get(),my_box3.get(),my_box4.get()  )
        my_label.config(text=value)
    except:
        my_label.config(text='Enter valid numbers')


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


#//////////////////////////////////////////////////////////////////////
# creating a label
my_label = Label(root, text='', font=('Roboto', 12), fg='black')
my_label.pack(pady=10)


# calling submit function
my_button = Button(root, text="Submit", font=('roboto', 10), command=submit)
my_button.pack(pady=20)

root.mainloop()
