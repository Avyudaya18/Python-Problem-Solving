n=int(input("Enter a number "))
Bin=0
mp=1
while(n!=0):
    rem=n%2
    Bin+=(mp*rem)
    n//=2
    mp*=10
    
if len(str(Bin))>=3:
    print(Bin)
# else:
#     remain=3-len(str(bin))
#     print(int(("0"*remain)+str(bin)))