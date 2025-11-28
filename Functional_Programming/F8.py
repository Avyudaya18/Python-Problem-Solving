#Integer to Binary
def Convert(n,res=0):
    while(n!=0):
        rem=n%2
        res=(res*10)+rem
        n//=2
    return res
print(Convert(5))
        