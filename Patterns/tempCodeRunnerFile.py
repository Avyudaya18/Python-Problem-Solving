lines=int(input("Enter the no.of lines: "))
row=lines
while(row>-1):
    sp=0
    while(sp<lines-row):
        print(" ",end=' ')
        sp+=1
    st=0
    while(st<row*2-1):
        print("*",end=' ')
        st+=1
    print()
    row-=1