class Practice:
    def m1(self):
        print("No Arguments")
    def m1(self,a,b):
        print("Two Arguments")
    def m1(self,a):
        print("One Argument")
p1=Practice()
p1.m1(2)

#Output: One Argument
