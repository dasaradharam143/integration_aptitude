from subprocess import call
import tkinter as tk
from tkinter import *

root = tk.Tk()
root.title('Aptitude')
root.geometry('600x600')


def average_clicked(value):
    if value == 1:
        # root.destroy()
        call(['python', 'average_of_numbers_tk.py'])
    elif value == 2:
        call(['python', 'total_sum_of_numbers_tk.py'])
    elif value == 3:
        call(['python', 'missing_numbers_from_average_tk.py'])
    elif value == 4:
        call(['python', 'missing_number_using_averages_tk.py'])
    elif value == 5:
        call(['python', 'average_reciprocal_tk.py'])
    elif value == 6:
        call(['python', 'avg_of_sum_of_squares_tk.py'])
    elif value == 7:
        call(['python', 'mean_average_tk.py'])
    elif value == 8:
        call(['python', 'find_missing_number_in_mean_average_tk.py'])
    elif value == 9:
        call(['python', 'find_correct_average_tk.py'])
    elif value == 10:
        call(['python', 'finding_x_tk.py'])
    elif value == 11:
        pass


def races_clicked(value):
    if value == 1:
        call(['python', 'members_game_tk.py'])
    elif value == 2:
        call(['python', 'three_contestants_same_distance_tk.py'])


def stocks_clicked(value):
    if value == 1:
        call(['python', 'find_cost_price.py'])
    elif value == 2:
        call(['python', 'find_stock_value_on_selling_price.py'])
    elif value == 3:
        call(['python', 'find_number_of_shares.py'])
    elif value == 4:
        call(['python', 'find_income_or_dividend_on_investment.py'])
    elif value == 5:
        call(['python', 'find_total_investment_on_debenture.py'])
    elif value == 6:
        call(['python', 'find_annual_income.py'])
    elif value == 7:
        call(['python', 'find_loss_or_gain_on_amount_invested_in_bank_and_Stock.py'])
    elif value == 8:
        call(['python', 'find_investment_on_income.py'])
    elif value == 9:
        call(['python', 'find_interest_obtained_on_faceValue.py'])
    elif value == 10:
        call(['python', 'find_part_of_amount_in_total_investment.py'])
    elif value == 11:
        call(['python', 'find_maximum_return.py'])
    elif value == 12:
        call(['python', 'find_ratios_of_investments.py'])
    elif value == 13:
        call(['python', 'find_better_investment_Stock.py'])
    elif value == 14:
        call(['python', 'find_change_in_income.py'])
    elif value == 15:
        call(['python', 'find_change_in_income_on_service_charge.py'])
    elif value == 16:
        call(['python', ''])
        pass

def average():
    v = IntVar()
    Radiobutton(root, text='average of numbers', variable=v, value=1,
                command=lambda: average_clicked(v.get())).pack()
    Radiobutton(root, text='total sum of numbers', variable=v, value=2,
                command=lambda: average_clicked(v.get())).pack()
    Radiobutton(root, text='missing number from average', variable=v, value=3,
                command=lambda: average_clicked(v.get())).pack()
    Radiobutton(root, text='missing number using averages', variable=v, value=4,
                command=lambda: average_clicked(v.get())).pack()
    Radiobutton(root, text='average of reciprocal of numbers', variable=v, value=5,
                command=lambda: average_clicked(v.get())).pack()
    Radiobutton(root, text='avg of sum of n powers', variable=v, value=6,
                command=lambda: average_clicked(v.get())).pack()
    Radiobutton(root, text='mean average', variable=v, value=7,
                command=lambda: average_clicked(v.get())).pack()
    Radiobutton(root, text='missing number in mean average', variable=v, value=8,
                command=lambda: average_clicked(v.get())).pack()
    Radiobutton(root, text='correct average', variable=v, value=9,
                command=lambda: average_clicked(v.get())).pack()
    Radiobutton(root, text='finding x numbers', variable=v, value=10,
                command=lambda: average_clicked(v.get())).pack()


def races():
    v = IntVar()
    Radiobutton(root, text='members game', variable=v, value=1,
                command=lambda: races_clicked(v.get())).pack()
    Radiobutton(root, text='three contestants same distance', variable=v, value=2,
                command=lambda: races_clicked(v.get())).pack()
    Radiobutton(root, text='races3', variable=v, value=3,
                command=lambda: races_clicked(v.get())).pack()
    Radiobutton(root, text='races4', variable=v, value=4,
                command=lambda: races_clicked(v.get())).pack()


def stocks():
    v = IntVar()
    Radiobutton(root, text='find_cost_price', variable=v, value=1,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_stock_value_on_selling_price', variable=v, value=2,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_number_of_shares', variable=v, value=3,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_income_or_dividend_on_investment', variable=v, value=4,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_total_investment_on_debenture', variable=v, value=5,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_annual_income', variable=v, value=6,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_loss_or_gain_on_amount_invested_in_bank_and_Stock', variable=v, value=7,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_investment_on_income', variable=v, value=8,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_interest_obtained_on_faceValu', variable=v, value=9,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_part_of_amount_in_total_investment', variable=v, value=10,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_maximum_return', variable=v, value=11,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_ratios_of_investments', variable=v, value=12,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_better_investment_Stock', variable=v, value=13,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_change_in_income', variable=v, value=14,
                command=lambda: stocks_clicked(v.get())).pack()
    Radiobutton(root, text='find_change_in_income_on_service_charge', variable=v, value=15,
                command=lambda: stocks_clicked(v.get())).pack()


label = Label(root, text='Aptitude Topics', font=('bold', 18))
label.pack(pady=10)

button1 = Button(root, text='1.Averages', font=('roboto', 10), bg='sky blue', command=average)
button1.pack(pady=8)

button2 = Button(root, text='2.Races and Games', font=('roboto', 10), bg='sky blue', command=races)
button2.pack(pady=8)

button3 = Button(root, text='3.Stocks and Shares', font=('roboto', 10), bg='sky blue', command=stocks)
button3.pack(pady=8)

root.mainloop()
