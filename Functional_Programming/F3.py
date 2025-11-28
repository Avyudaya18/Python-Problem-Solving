def Add(num,sum=0):
    if(num<0):
        num*=(-1)
    while(num!=0):
        rem=num%10
        sum+=rem
        num//=10
    return sum
n=int(input("Enter a number"))
if(n<0):
    res=Add(n)*(-1)
else:
    res=Add(n)
print("Sum of all is:",res)