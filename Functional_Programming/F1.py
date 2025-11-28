def Prime(num):
    if num>2:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return "Not a Prime!"
        
        return "Prime"
    else:
        return "Not a Prime!"
    
print(Prime(100))