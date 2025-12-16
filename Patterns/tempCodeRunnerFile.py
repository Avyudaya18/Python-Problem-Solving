lines=int(input("Enter the no.of lines: "))
for row in range(lines,-1,-1):
    for sp in range(0,lines-row):
        print(" ",end=" ")
    for st in range(row*2-1):
        print("*",end=" ")
    print()