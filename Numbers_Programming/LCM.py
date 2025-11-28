Num1=int(input("Enter a number "))
Num2=int(input("Enter a number "))
pro=Num1*Num2
for lcm in range(max(Num1,Num2),pro+1):
    if lcm%Num1==0 and lcm%Num2==0:
        print("LCM is ",lcm)
        break
