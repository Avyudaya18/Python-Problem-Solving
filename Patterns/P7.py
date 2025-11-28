lines=int(input("Enter the no.of lines: "))
for row in range(1,lines+1):
    if(row<=lines//2+1):
        for sp in range((lines//2)-row+1):
            print(" ",end=" ")
        for st in range(row*2-1):
            print("*",end=" ")
        print()
    else:
        for sp in range(row-(lines//2+1)):
            print(" ",end=" ")
            
        for st1 in range((lines-row)*2+1):
            print("*",end=" ")
        print()


# lines=int(input("Enter the number of lines: "))
# row=1
# space=(lines//2)
# star=1
# while(row<lines+1): 
#     sp=0
#     while(sp<space):
#         print(" ",end=" ")
#         sp+=1
#     st=0
#     while(st<star):
#         print("*",end=" ")
#         st+=1
#     print()
#     row+=1
#     if row<=(lines//2)+1:
#         space-=1
#         star+=2
#     else:
#         space+=1
#         star-=2
    
