n=int(input("Enter a number"))
if n>1:
    for val in range(2,int(n**0.5)):
        if n%val==0:
            print("Not a Prime Number")
    else:
        print("Prime Number")
else:
    print("Not a prime! ")