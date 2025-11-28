#Reverse a Number
def Reverse(n,rev=0):
    while(n!=0):
        rem=n%10
        rev=(rev*10)+rem
        n//=10
    return rev

num=int(input("Enter a number: "))
print(Reverse(num))