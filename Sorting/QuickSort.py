def Quick(L):
    if len(L)<2:
        return L
    pivot=L[0]
    left=[ele for ele in L[1:] if pivot>ele]
    right=[ele for ele in L[1:] if pivot<=ele]
    return Quick(left)+[pivot]+Quick(right)

L=[5,7,4,2,420,-8,7,18]
print(Quick(L))