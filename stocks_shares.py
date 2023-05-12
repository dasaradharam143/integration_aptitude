from fractions import Fraction


def find_cost_price():
    face_value = float(input("Enter the FaceValue : "))
    discount = float(input("Enter the Discount : "))
    brokerage = float(input("Enter the Brokerage : "))
    cost_price = float(face_value - discount + brokerage)
    print("Cost_Price : " + str(cost_price))


def find_stock_value():
    selling_price = float(input("Enter the SellingPrice : "))
    brokerage = float(input("Enter the Brokerage : "))
    share_value = float(selling_price - brokerage)
    print("stock_value : " + str(share_value))


def find_investment():
    income1 = Fraction(input("Income1 or Earn1 or obtain1 :"))
    investment1 = float(input("Investment1 or Stock1 : "))
    income2 = Fraction(input("Income2 or Earn2 or obtain2 : "))
    investment2 = float((investment1 / income1) * income2)
    print("Investment2 or Stock2 :" + str(investment2))


def find_dividend():
    investment1 = float(input("Investment1 : "))
    income1 = float(input("Income1 : "))
    investment2 = float(input("Investment2 : "))
    income2 = float((income1 / investment1) * investment2)
    print("Income2 : " + str(income2))
    print("Dividend :" + str(income2) + "%")


def find_annual_income():
    total_investment = float(input("Total Investment : "))
    investment_in_one_share = float(input("Investment in 1'share : "))
    face_value_of_one_share = float(input("FaceValue of 1'Share  : "))
    dividend = float(input("Dividend : "))
    annual_income = float((dividend / 100) * ((total_investment / investment_in_one_share) * face_value_of_one_share))
    print("Annual_Income : " + str(annual_income))


def find_income():
    investment1 = float(input("Investment1 :"))
    income1 = float(input("Income1: "))
    investment2 = float(input("Investment2 : "))
    income2 = float((income1 / investment1) * investment2)
    print("Income2 :" + str(income2))


def find_number_of_shares():
    purchased_total_share_value = float(input("Enter the purchased_total_share_value : "))
    cost_of_each_share = float(input("Enter the cost on EachShare : "))
    brokerage = float(input("Enter the Brokerage : "))
    number_of_share_values = purchased_total_share_value / (cost_of_each_share+((brokerage*cost_of_each_share)/100))
    print("Number of ShareValues : " + str(number_of_share_values))


def find_total_investment_on_debenture():
    total_income = float(input("Total Income : "))
    one_share_income = float(input("each income on single investment : "))
    x = float(input("cost of each debenture : "))
    y = float(input("Brokerage : "))
    number_of_debenture = float(total_income / one_share_income)
    cost_of_each_debenture = float(x + ((y * x) / 100))
    total_investment_on_debentures = (cost_of_each_debenture * number_of_debenture)
    print("T.Investment on Debentures : " + str(total_investment_on_debentures))


def find_interest_obtained_on_faceValue():
    number_of_shares = float(input("No of Shares : "))
    each_share_value = float(input("each share value : "))
    discount = float(input("Discount : "))
    investment = float(number_of_shares * (each_share_value - discount))
    print("investment :" + str(investment))
    face_value = float(number_of_shares * each_share_value)
    print("Face Value :" + str(face_value))
    dividend_percentage = Fraction(input("Dividend % : "))
    dividend = Fraction((dividend_percentage / 100) * face_value)
    interest_obtained = float(dividend * 100) / investment
    print("Interest Obtained :" + str(interest_obtained) + "%")


def find_part_of_amount_in_total_investment():
    total_investment = float(input("Total Investment : "))
    first_stock_rate = float(input("1st dividend part on market Value by 1st investment : "))
    first_stock_market_value = float(input("first Market Value : "))
    second_stock_rate = float(input("2st dividend part on market Value by 2nd investment : "))
    second_stock_market_value = float(input("Second Market Value : "))
    total_dividend = float(input("Total Income or Dividend (enter 0 to skip): "))
    if total_dividend != 0:
        x = ((first_stock_market_value * second_stock_market_value * total_dividend)
             - (second_stock_rate * first_stock_market_value * total_investment)) / \
            ((first_stock_rate * second_stock_market_value) - (second_stock_rate * first_stock_market_value))
        print("1stPart invested on total Amount : " + str(x))
    else:
        y = (second_stock_rate * total_investment * first_stock_market_value * second_stock_market_value) /\
            ((second_stock_market_value * first_stock_rate * second_stock_market_value) +
             (second_stock_market_value * second_stock_rate * first_stock_market_value))
        print("1stPart invested on total Amount : " + str(y))


def find_better_investment_stock():
    first_stock_rate = Fraction(input("enter AnnualIncome on 1's share a1 : "))
    first_stock_market_value = float(input("enter Market_value b1 : "))
    second_stock_rate = Fraction(input("enter AnnualIncome on 1's share a2 : "))
    second_stock_market_value = float(input("enter Market_value b2 : "))
    income_tax_rate = float(input("income_tax_rate : "))
    if income_tax_rate == 0:
        x = (first_stock_rate * first_stock_market_value * second_stock_market_value) / first_stock_market_value
        print("annual_income 1st stock : " + str(x))
        y = (second_stock_rate * first_stock_market_value * second_stock_market_value) / second_stock_market_value
        print("annual_income 2nd stock : " + str(y))
    else:
        x = (first_stock_rate*second_stock_market_value)-((0.01*income_tax_rate)*
                                                          (first_stock_rate*second_stock_market_value))
        print("x_annual_income 1st stock : " + str(x))
        y = (second_stock_rate*first_stock_market_value)
        print("y_annual_income 2nd stock : " + str(y))
    if x > y:
        print(str(first_stock_rate) + " Stock at " + str(first_stock_market_value) + " is better")
    else:
        print(str(second_stock_rate) + " Stock at " + str(second_stock_market_value) + " is better")


def find_loss_or_gain_on_amount_invested_in_bank_and_stock():
    total_investment = float(input("Total Investment : "))
    bank_interest = float(input("interest on investment by bank : "))
    face_value = float(input("Face Value : "))
    one_share_value = float(input("Cost of Each Share : "))
    dividend = float(input("Dividend % on Face Value : "))
    bank_income = float((total_investment * bank_interest) / 100)
    stock_income = float(((dividend * face_value) / 100) * (total_investment / one_share_value))
    print("bank_income : " + str(bank_income))
    print("Total Income on Stock : " + str(stock_income))
    if bank_income > stock_income:
        difference_in_income = float(bank_income - stock_income)
        print("LOSS : " + str(difference_in_income))
    else:
        difference_in_income = float(stock_income - bank_income)
        print("GAIN : " + str(difference_in_income))


def find_maximum_return():
    investing_amount = int(input('total investment = '))
    comparative_percentage_condition = int(input('conditional_percentage_investment_by_bond(a)_on_bond(b) = '))
    investment_in_bond_a = 100 * investing_amount / (comparative_percentage_condition + 100)
    investment_in_bond_b = investing_amount - investment_in_bond_a
    print((investment_in_bond_a, investment_in_bond_b))
    annual_return_percent_on_bond_a = int(input('percentage on bond a = '))
    annual_return_percent_on_bond_b = int(input('percentage on bond b = '))
    maximum_return = (annual_return_percent_on_bond_a * investment_in_bond_a / 100) +\
        (annual_return_percent_on_bond_b * investment_in_bond_b / 100)
    print("Maximum Return : " + str(maximum_return))


def find_ratios_of_investments():
    stock_value_a = Fraction(input('Stock value a = '))
    dividend_a = Fraction(input('Dividend % a = '))
    stock_value_b = Fraction(input('Stock Value b = '))
    dividend_b = Fraction(input('Dividend % b = '))
    investment_a = (stock_value_a /dividend_a)  # take 1'rupee is income of both a and b stock value then
    investment_b = stock_value_b /dividend_b    # their investment is stock_value / dividend equals income of 1'rupee
    ratios_of_investments = investment_a / investment_b
    print("Ratios of Investments : " + str(ratios_of_investments))


def find_change_in_income():
    investment = float(input("1st Investment : "))  # total Stock value
    dividend_percentage_of_first_stock_value = float(input("Annual Dividend % on one Share of A : "))
    first_stock_value = float(input("one Share Value of 1st Investment : "))
    sold_one_stock = float(input("One Share Value Sold at : "))
    new_stock_value_dividend_percentage = float(input("Dividend % of One New Stock Value : "))
    new_stock_value_invested = float(input("New Stock Value Invested : "))
    number_of_shares = (investment / first_stock_value)
    original_income = dividend_percentage_of_first_stock_value * number_of_shares
    print('original_income : ' + str(original_income))
    new_income = (sold_one_stock*number_of_shares*new_stock_value_dividend_percentage) / new_stock_value_invested
    print('new_income : ' + str(new_income))
    change_in_income = (new_income - original_income)
    print("change in Income : " + str(change_in_income))


def find_change_in_income_on_service_charge():
    sold_stock_value = float(input("total Shares sold at : "))
    stock_rate = float(input("Dividend % on 1st Invested : "))
    old_stock_value = float(input("one Share Value of 1st Invested : "))
    new_stock_rate = float(input("Dividend % on one New Stock Value: "))
    new_stock_value = float(input("one Share Value of 2nd Investment: "))
    service_charges = float(input("Service Charges % of Face value: "))
    face_value = 100
    number_of_shares = sold_stock_value / face_value  # no. of shares sold
    stock_value_purchased = (old_stock_value - service_charges) * number_of_shares
    number_of_new_shares_purchased = stock_value_purchased / (new_stock_value + service_charges)
    original_income = (sold_stock_value * stock_rate) / 100
    print('original_income : ' + str(original_income))
    new_income = (new_stock_rate * number_of_new_shares_purchased)
    print('new_income : '+ str(new_income))
    change_in_income = (new_income - original_income)
    print("change in Income : " + str(change_in_income))


given_data = input("   CostPrice enter 1 \nor Sold Share_Value enter 2 \nor Investment enter 3 \nor Dividend enter 4 "
                   "\nor find_Annual_Income_/_FV enter 5 \nor find Income enter 6 \nor number_of_shares enter 7 "
                   "\nor Total_Debenture enter 8 \nor Interest_on_faceValue enter 9 \n"
                   "or Find_X_Part_in_total_Investment enter 10 \nor find which Stock is Better enter 11 \nor "
                   "find Loss or gain on amount invested in bank & Stock enter 12 : \n"
                   "or find find_maximum_return enter 13 \nor find find_ratios_of_investments enter 14 "
                   "\nor find change in Income enter 15 : \nor find change in income on service charge enter 16 \n  = ")
if given_data == '1':
    find_cost_price()
elif given_data == '2':
    find_stock_value()
elif given_data == '3':
    find_investment()
elif given_data == '4':
    find_dividend()
elif given_data == '5':
    find_annual_income()
elif given_data == '6':
    find_income()
elif given_data == "7":
    find_number_of_shares()
elif given_data == "8":
    find_total_investment_on_debenture()
elif given_data == "9":
    find_interest_obtained_on_faceValue()
elif given_data == "10":
    find_part_of_amount_in_total_investment()
elif given_data == "11":
    find_better_investment_stock()
elif given_data == "12":
    find_loss_or_gain_on_amount_invested_in_bank_and_stock()
elif given_data == "13":
    find_maximum_return()
elif given_data == "14":
    find_ratios_of_investments()
elif given_data == "15":
    find_change_in_income()
elif given_data == "16":
    find_change_in_income_on_service_charge()
else:
    print('enter a valid input')
