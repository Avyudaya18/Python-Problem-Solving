#Armstrong Number
def Armstrong(num):
    temp=0
    pow=len(str(num))
    while(num!=0):
        rem=num%10
        temp+=rem**pow
        num//=10
    return temp
n=int(input("Enter the number: "))
res=Armstrong(n)
if(n==res):
    print("Armstrong Number")
else:
    print("Not a Armstrong")
        