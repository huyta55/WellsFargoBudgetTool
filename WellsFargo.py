import csv

# Prompting the user to input name of desired CSV file to open, then opening it
# fileName = input("What file would you like to open: ")
fileName = "latest"
fileName = "csv/" + fileName + ".csv"
transactionFile = open(fileName, 'r')
type(transactionFile)
csvReader = csv.reader(transactionFile)

# Reading the CSV file and placing the data into correct storage containers
# Declaring variables for storing the data
dates = []
amounts = []
fromWho = []
for index, transaction in enumerate(transactionFile):
    transList = transaction.split(",", 5)
    dates.append(transList[0])
    amounts.append(transList[1])
    fromWho.append(transList[4])
print("lol")
