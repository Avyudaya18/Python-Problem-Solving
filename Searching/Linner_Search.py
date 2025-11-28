l=[10,20,30,40,50,60]
target=40
for ind in range(len(l)):
    if l[ind]==target:
        print(ind)
        break
else:
    print(-1)