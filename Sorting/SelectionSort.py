L=[7,420,-5,24,7,27]
for ei in range(0,len(L)-1):
    least=ei
    for si in range(ei+1,len(L)):
        if L[least]>L[si]:
            least=si
    L[least],L[ei]=L[ei],L[least]
    
print(L)