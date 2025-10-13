class Division:
    def __init__(self,a,b):
        self.n = a
        self.d = b
    def division(self):
        return self.n/self.d
class Mod_div:
    def __init__(self,a,b):
        self.n = a
        self.d = b
    def division(self):
        return self.n%self.d
class calci(Mod_div, Division):
    def __inti__(self,a,b):
        self.n = a
        self.d = b
c1=calci(20,10)
print(c1.division())
print(type(c1))
d1=Division(20,45)
print(type(d1))



#Output:
#0
#<class '__main__.calci'>
#<class '__main__.Division'>
