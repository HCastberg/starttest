#nested loops = The "innter loop" will finish all of its iterations before finishing iteration of the "outer loop"


rows = int(input("How many rows?: "))
colums = int(input("How many colums?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(colums):
        print(symbol, end="")
    print()