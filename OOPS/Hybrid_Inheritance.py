class A:
    pass
class B(A):
    pass
class C(A):
    pass
class E(B,C):
    pass
class F(B,C):
    pass
class G(E,F):
    pass

obj=G()
print(G.mro())