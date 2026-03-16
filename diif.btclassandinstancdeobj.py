class test:
    x= 20
    def __init__(self, a, b):
        self.a=a
        self.b=b
    def show(self):
        print(self.a,self.b)
print(test.x)
t1=test(4,5)
t1.show()
print(t1.a)
print(t1.b)


#Output:
#   20
#   4 5
#   4
#   5
