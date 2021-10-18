"""
This is the bill class which will include the subtotal, tip, an additional fees field.
"""


class Bill():
    def __init__(self, subtotal, tips, fees):
        self.subtotal = subtotal
        self.tips = tips
        self.fees = fees
        self.total = subtotal + tips + fees
        self.payees = {}

    def add_user(self, username, user_subtotal):
        self.payees[username] = {user_subtotal, self.subtotal/user_subtotal}
