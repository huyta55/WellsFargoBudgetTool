def find_category(from_who, date, amount):
    # Making master lists for comparisons with transactions
    food_list = ["PUBLIX", "SAMS", "ALDI", "SPROUTS", "ORIENTAL"]
    shopping_list = ["NIKE", "ADIDAS", "OLD NAVY", "Amzn.com", "TARGET", "WALMART", "TJMAXX"]
    gas_list = ["CIRCLE K", "7-ELEVEN"]

    food = any(element in from_who for element in food_list)
    shopping = any(element in from_who for element in shopping_list)
    gas = any(element in from_who for element in gas_list)
    if food:
        # Checks whether the Sam's transaction was for food or gas
        if "SAMS" in from_who:
            print("Transaction: $", amount, " on ", date)
            return input("What category is this Sam's Club transaction? Gas (3) or Groceries (1): ")
        return 1
    elif shopping:
        return 2
    elif gas:
        return 3
    else:
        return 0


class Transaction(object):

    def __init__(self, date, amount, who):
        date.replace('"', "")
        amount.replace('"', "")
        amount = float(amount)
        self.date = date
        self.amount = amount
        self.who = who
        self.category = find_category(who, date, amount)

    def edit_date(self, new_date):
        self.date = new_date

    def edit_amount(self, new_amount):
        self.amount = new_amount

    def edit_who(self, new_who):
        self.who = new_who

    def edit_category(self, new_category):
        self.category = new_category

    def print_transaction(self):
        print(self.amount, " ", self.who, " ", self.date)