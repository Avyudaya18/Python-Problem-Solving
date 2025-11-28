Num=int(input("Enter a number "))
temp=Num
Strong=0
while(Num!=0):
    rem=Num%10
    fact=1
    for val in range(1,rem+1):
        fact*=val
    Strong+=fact
    Num//=10
if Strong==temp:
    print(temp,"is a Strong Number")
else:
    print("Not a Strong Number")