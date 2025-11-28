# line=int(input("Enter the number of rows: "))
# for row in range(1,line//2+2):
#     for st in range(row):
#         print("*",end=' ')
#     print()
# for row in range((line//2),0,-1):
#     for st in range(row):
#         print("*",end=' ')
#     print()


line=int(input("Enter the number of rows: "))
for row in range(1,line//2+2):
    for sp in range(line-row):
        print(" ",end=' ')
    for st in range(row):
        print("*",end=' ')
    print()
for row in range((line//2),0,-1):
    for sp in range(line-row):
        print(" ",end=' ')
    for st in range(row):
        print("*",end=' ')
    print()