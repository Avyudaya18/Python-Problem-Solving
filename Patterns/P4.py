lines=int(input("Enter the no.of lines: "))
for row in range(1,lines+1):
    for sp in range(row-1):
        print(" ",end=' ')
    for st in range(lines+1-row):
        print("*",end=" ")
    print()