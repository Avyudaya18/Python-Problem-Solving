
n=int(input("Enter the no of lines: "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if  row==col or col==1 or row==n:
            print("*",end=' ')
        else:
            print(" ",end=' ')
            
    print()