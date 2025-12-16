# lines=int(input("Enter the no.of lines: "))
# for row in range(1,lines+1):
#     for sp in range(lines-row):
#         print(" ",end=" ")
#     for st in range(row*2-1):
#         print("*",end=" ")
#     print()
    

lines=int(input("Enter the no.of lines: "))
row=1
while(row<=lines):
    sp=0
    while(sp<lines-row):
        print(" ",end=" ")
        sp+=1
    st=0
    while(st<row*2-1):
        print("*",end=' ')
        st+=1
    print()
    row+=1
