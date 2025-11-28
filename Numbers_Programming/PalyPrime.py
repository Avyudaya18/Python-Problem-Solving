num=int(input("Enter a number "))
temp=num
rev=0
while(num!=0):
    rem=num%10
    rev=(rev*10)+rem
    num//=10
print(rev)
if temp==rev:
    for i in range(2,int(temp**0.5)):
        if temp%i==0:
            break
    else:
        print(temp," is a PalyPrime Number")

else:
    print("Not a Palyprime")