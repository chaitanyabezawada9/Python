class Test:
    def sum(self,a=0,b=0,c=0):
        if(a!=0 and b!=0 and c!=0):
            print("Three numbers are given")
        elif(a!=0 and b!=0):
            print("Two numbers are given")
        else:
            print("Provide atleast two numbers")

p1=Test()
p1.sum(15,26,28)

#Output: Three numbers are given
        
