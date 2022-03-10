import csv
import Transaction


def find_category(from_who):
    test_list = ["Publix", "SAMS", "ALDI", "SPROUTS", "ORIENTAL"]
    food = any(element in from_who for element in test_list)
    if food:
        return 1
    else:
        return 0


def main():
    # Prompting the user to input name of desired CSV file to open, then opening it
    # fileName = input("What file would you like to open: ")
    file_name = "latest"
    file_name = "csv/" + file_name + ".csv"
    transaction_file = open(file_name, 'r')
    type(transaction_file)
    csvReader = csv.reader(transaction_file)

    # Reading the CSV file and placing the data into correct storage containers
    # Declaring variables for storing the data
    dates = []
    amounts = []
    from_who = []
    transactions = []
    for index, transaction in enumerate(transaction_file):
        trans_list = transaction.split(",", 5)
        dates.append(trans_list[0])
        amounts.append(trans_list[1])
        from_who.append(trans_list[4])
    # Creating transaction objects that stores corresponding information about the transaction
    for index, date in enumerate(dates):
        new_transaction = Transaction.Transaction(dates[index], amounts[index], from_who[index], find_category(from_who[index]))
        transactions.append(new_transaction)


print("done")
