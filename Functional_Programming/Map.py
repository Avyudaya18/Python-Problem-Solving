# def sq(n):
#     return n**2

# mapobj=map(sq,range(1,6))
# print(list(mapobj))
# for i in mapobj:
#     print(i)

# def evenodd(n):
#    return print("Even") if n%2==0 else print("Odd")

# mapobj=map(evenodd,range(1,10))
# print(list(mapobj))


# def Addall(n,sum=0):
#     while(n!=0):
#         rem=n%10
#         sum+=rem
#         n//=10
#     return sum
# print(list(map(Addall,[1122,2211,1212])))


# print(list(map(lambda n1,n2:n1+n2,[1,2,3,4],[4,3,2,1])))

# print("\n".join(list(map(lambda a:"* "*a,range(1,5)))))

# n=int(input("Enter the number of row: "))
# print("\n".join(list(map(lambda sp,st:"  "*sp+"* "*st,range(n),range(n,0,-1)))))


#FILTER()
# def a(n):
#     if n%2==0:
#         return True
#     else:
#         return False
# print(list(filter(a,range(1,5))))

# print(list(filter(len, input().split(' '))))

import functools
num=int(input("Enter the no."))
print(functools.reduce(lambda n1,n2:n1*n2,range(1,6),1))