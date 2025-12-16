lines=int(input("Enter the no.of lines: "))
for row in range(1,lines+1):
    for sp in range(lines-row):
        print(" ",end=" ")
    for st in range(row):
        print("*",end=" ")
    print()