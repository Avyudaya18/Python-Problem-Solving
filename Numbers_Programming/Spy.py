n=int(input("Enter a number "))
add=0
mul=1
while(n!=0):
    rem=n%10
    add+=rem
    mul*=rem
    n//=10
if add==mul:
    print("Spy Number")
else:
    print("Not a Spy Number")