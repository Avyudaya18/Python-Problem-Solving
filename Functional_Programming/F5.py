#Disarum Number
def Disarum(num):
    temp=0
    while(num!=0):
        pow=len(str(num))
        rem=num%10
        temp+=rem**pow
        num//=10
    return temp
n=int(input("Enter the number: "))
res=Disarum(n)
if(n==res):
    print("Disarum Number")
else:
    print("Not a Disarum")
        