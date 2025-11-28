lines=int(input("Enter the no. of lines: "))
for row in range(1,lines+1):
    for sp in range(lines-row):
        print(" ",end=" ")
    number=1
    for num in range(1,row*2):
        print(number,end=' ')
        number+=1
    print()