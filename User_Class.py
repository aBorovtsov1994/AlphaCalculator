"""
This is the user class that will be implemented to keep track of the User's menu items and costs as well as his ratio of
expenditure.
"""


class User():

    def __init(self, items):
        self.items = items
        self.ratio = 0.0

    def calc_ratio(self):
        result = 0.0
        for item in self.ratio.values():
            result += item
        return result / len(self.ratio.values())