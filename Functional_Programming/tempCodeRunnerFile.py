def Convert(n,pow=0):
    if n==0:
        return 0
    return (n%10)*(2**pow)+Convert(n//10,pow+1)

print(Convert(110))