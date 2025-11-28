n=int(input("Enter a number "))
temp=n
pow=len(str(n))
sum=0
while(n!=0):
    rem=n%10
    sum+=rem**pow
    n//=10

if temp==sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong")
