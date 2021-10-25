"""
This calculator is going to take a bill and split it among a set amount of users (user-defined). It will calculate the
ratio each person owes and then use those ratios to calculate how much of the tips/fees each user owes and adds that
to the total they are owed.
"""
num_of_users = 0
bill_subtotal = 0
tips_amount = 0
fees_amount = 0


def check_input_int(user_input):
    while True:
        if user_input.isnumeric():
            return user_input
        else:
            print("Please enter a valid number")


print("Hello and welcome to my Alpha calculator! Please go ahead and enter the subtotal!")

num_of_users = check_input_int(input("Please enter the amount of users for this bill.\n"))

if __name__ == '__main__':
    print("The main program has run!")
