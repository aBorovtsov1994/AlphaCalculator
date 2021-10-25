"""
This calculator is going to take a bill and split it among a set amount of users (user-defined). It will calculate the
ratio each person owes and then use those ratios to calculate how much of the tips/fees each user owes and adds that
to the total they are owed.
"""
num_of_users = 0
bill_subtotal = 0
tips_amount = 0
fees_amount = 0

print("Hello and welcome to my Alpha calculator! Please go ahead and enter the subtotal!")

while True:
    num_of_users = input("Please enter the amount of users for this bill.\n")
    if num_of_users.isnumeric():
        break
    else:
        print("Please enter a valid number")
print(num_of_users) ## check to see if this works


if __name__ == '__main__':
    print("The main program has run!")