n=int(input("Enter a number "))
Bin=0
count=0
while(n!=0):
    rem=n%2
    if(rem==1):
        count+=1
    n//=2
if count%2==0:
    print("Evil Number")
else:
    print("Odieous Number")
    