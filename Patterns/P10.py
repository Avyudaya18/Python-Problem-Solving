n=int(input("Enter the no of lines: "))
star=5
space=0
for row in range(1,n+1):
    for sp in range(space):
        print(" ",end=' ')
    for st in range(star):
        print('*',end=' ')
    print()
    
    if row<(n//2)+1:
        star-=2
        space+=1
    else:
        star+=2
        space-=1