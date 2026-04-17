# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   innter loop:

for x in range(3):
    for i in range(1, 10):
        print(i, end="")    # to get all on the same line
    print()


rows = int(input("Enter num rows: "))
columns = int(input("Enter num columns: "))
symbol = input("Enter symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()
