# num=int(input("Enter a Number"))
# fact=1
# for val in range(1,num+1):
#     fact*=val
# print("Factorial is: ",fact)

n=int(input("Enter a number "))
i=1
fact=1
while(i<=n):
    fact*=i
    i+=1
print(fact)