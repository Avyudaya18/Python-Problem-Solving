# l=[10,20,30,40,50,60]
# target=40
# s_ind=0
# e_ind=len(l)-1
# while(s_ind<=e_ind):
#     mid=(s_ind+e_ind)//2

#     if(l[mid]>target):
#         e_ind=mid-1
#     elif(l[mid]<target):
#         s_ind=mid+1
#     else:
#         print(mid)
#         break


def Binary(l,target,s_ind,e_ind):
    if s_ind>e_ind:
        return -1

    mid=(s_ind+e_ind)//2
    if l[mid]>target:
        return Binary(l,target,s_ind,mid-1)
    elif l[mid]<target:
        return Binary(l,target,mid+1,e_ind)
    else:
        return mid

l=[10,20,30,40,50,60]
target=40
s_ind=0
e_ind=len(l)-1
print(Binary(l,target,s_ind,e_ind))
