class father:
    def Responsibility(self):
        print("Earning")
        print("Caring")
class mother:
    def Responsibility(self):
        print("Cooking")
        print("Loving")
class child(father,mother):
    def Responsibility(self):
        father.Responsibility(self)
        mother.Responsibility(self)
        print("Playing")
        print("Study")
        
obj=child()
obj.Responsibility()
        