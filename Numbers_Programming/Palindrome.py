Num=int(input("Enter a number "))
temp=Num
rev=0
while (Num!=0):
    rem=Num%10
    rev=(rev*10)+rem
    Num//=10
if temp==rev:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")
