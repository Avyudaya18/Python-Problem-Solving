n=int(input("Enter a number "))
temp=n
sum=0
while(n!=0):
    pow=len(str(n))
    rem=n%10
    sum+=rem**pow
    n//=10

if temp==sum:
    print("Disarum Number")
else:
    print("Not an Disarum")