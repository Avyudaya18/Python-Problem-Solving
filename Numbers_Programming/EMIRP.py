num=int(input("Enter a number "))
temp=num
rev=0
while(num!=0):
    rem=num%10
    rev=(rev*10)+rem
    num//=10
if temp!=rev:
    for val in range(2,int(temp**0.5)):
        if temp%val==0:
            print("Not a EMIRP Number")
            break
    else:
        for val1 in range(2,int(rev**0.5)):
            if rev%val1==0:
                print("Not a EMIRP Number")
                break
        else:
            print(temp," is a EMIRP Number")
else:
    print("Not a EMIRP Number")
