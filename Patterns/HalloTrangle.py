n=int(input("Enter the no of lines: "))
for row in range(1,n+1):
    for sp in range(n-row):
        print(" ",end=' ')
    
    if(row<n):
        for star in range(1,row*2):
            if star==1 or star==row*2-1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
    else:
        for i in range(row*2-1):
            print("*",end=' ')
        print()