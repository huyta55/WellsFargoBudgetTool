class Transaction(object):
    def __init__(self, date, amount, who, category):
        self.date = date
        self.amount = amount
        self.who = who
        self.category = category

    def edit_date(self, new_date):
        self.date = new_date

    def edit_amount(self, new_amount):
        self.amount = new_amount

    def edit_who(self, new_who):
        self.who = new_who

    def edit_category(self, new_category):
        self.category = new_category
