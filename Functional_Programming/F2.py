def Factorial(n):
    fact=1
    for i in range(n,0,-1):
        fact*=i
    return fact

print("Factorial is: ",Factorial(5))