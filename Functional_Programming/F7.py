#Binary to Int
def Convert(n,res=0):
    pow=0
    while(n!=0):
        rem=n%10
        res+=rem*(2**pow)
        n//=10
        pow+=1    
    return res

num=int(input("Enter a number: "))
print(Convert(num))