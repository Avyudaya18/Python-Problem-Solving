def Interpolation(L,target,start,end):
    while(start<=end and L[start]<=target<L[end]):
        ind=int(start+((end-start)*(target-L[start])//(L[end]-L[start])))
        if L[ind]<target:
            start=ind+1
        elif L[ind]>target:
            end=ind-1
        else:
            return ind
            break
    else:
        return -1
    
L=[10,20,30,40,50,60,70,80,900,1000]
target=900
start_ind=0
end_ind=len(L)-1
print(Interpolation(L,target,start_ind,end_ind))