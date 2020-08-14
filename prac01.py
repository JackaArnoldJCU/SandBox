"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))


def question1():

    if sales >= 1000:
        print(sales * 1.15)
    elif sales <= 1000:
        print(sales * 1.1)


def question2():

    total_price = 0
    items = int(input("Number of items:"))
    for i in range(items):
        item_price = float(input("Price:"))
        total_price = total_price + item_price
        print("Total is $", total_price)


question1()
question2()
