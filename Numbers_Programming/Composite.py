n=int(input("Enter a number"))
if n>1:
    for val in range(2,n//2):
        if n%val==0:
            print("Composite No")
            break
    else:
        print("Not a Composite Number")
else:
    print("Not a Composite! ")