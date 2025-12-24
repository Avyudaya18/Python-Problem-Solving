L=[4,6,2,4,-3]
for ei in range(len(L)-1,0,-1):
    for ind in range(0,ei):
        if L[ind]>L[ind+1]:
            L[ind],L[ind+1]=L[ind+1],L[ind]
print(L)