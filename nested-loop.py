# nested loop = loop in loop (outer,inner)
#                       outer loop:
#                           inner loop:

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol: ")


for x in range(rows):

    for i in range(columns):
        print(symbol, end="")
    print()
