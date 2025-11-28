# def outer(args):
#     def inner(n1,n2):
#         if n2==0 and n1>0:
#             n2=n1
#             n1=0
#             args(n1,n2)
#         elif n1==0 and n2==0:
#             print("Not Possible")
#         else:
#             args(n1,n2)
#     return inner
# @outer
# def Sample(n1,n2):
#     print(n1%n2)
    
# Sample(3,4)
# Sample(0,5)
# Sample(5,0)
# Sample(0,0)


def Singleton(args):
    l=[]
    def inner():
        if len(l)==0:
            obj=args()
            l.append(obj)
        return l[0]
    return inner
@Singleton
class Sample():
    def __init__(self):
        print("Constructer is Called")
    def M1(self):
        print("M1 is called")
        
ob1=Sample()
ob2=Sample()
ob3=Sample()