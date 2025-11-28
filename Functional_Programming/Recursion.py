# def even(n):
#     if n==31:
#         return "Stop"
    
#     if(n%2==0):
#         print(n)
#     return even(n+1)
# print(even(1))

#FACTORIAL
# def Fact(n):
#     if n==1:
#         return 1
#     return n*Fact(n-1)

# n=int(input("Enter the number: "))
# print(Fact(n))


#ALL THE DIGIT IN A NUMBER
# def Number(n):
#     if n==0:
#         return 
#     print(n%10)
#     Number(n//10)
    
# Number(123456789)


#Add all
# def Add(n):
#     if n==0:
#         return 0
#     return (n%10)+Add(n//10)

# print(Add(12345))


# Armstrong
# def isArmstrong(n,pow):
#     if n==0:
#         return 0
#     return (n%10)**pow+isArmstrong(n//10,pow)

# n=int(input("Enter a number: "))
# pow=len(str(n))
# res=isArmstrong(n,pow)
# print("Armstrong Number") if n==res else print("Not an Armstrong")


#Disarum Number
# def isDisarum(n,pow):
#     if n==0:
#         return 0
#     return (n%10)**pow+isDisarum(n//10,pow-1)

# n=int(input("Enter a number: "))
# pow=len(str(n))
# res=isDisarum(n,pow)
# print("Disarum Number") if n==res else print("Not an Disarum")
   

#Integer to Binary
# def Convert(n,pow=1):
#     if n==0:
#         return 0
#     return (n%2)*pow+Convert(n//2,pow*10)

# print(Convert(4))


#Binary to Int
# def Convert(n,pow=0):
#     if n==0:
#         return 0
#     return (n%10)*(2**pow)+Convert(n//10,pow+1)

# print(Convert(110))


