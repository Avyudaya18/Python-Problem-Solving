# lines=int(input("Enter the no.of lines: "))
# for row in range(lines,0,-1):
#     for col in range(row):
#         print('*',end=" ")
#     print()

lines=int(input("Enter the no.of lines: "))
row=1
while(row<lines+1):
    col=0
    while(col<lines-row+1):
        print("*",end=" ")
        col+=1
    print()
    row+=1 