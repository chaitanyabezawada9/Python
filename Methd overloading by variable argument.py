class Test:
    def sum(self, *a):
        total=0
        for x in a:
            total=total+x
        print("Sum of numbers: ",total)
t1=Test()
t1.sum(5)
t1.sum(5,20,3)
t1.sum(5,26,28,80,99,88)

#Output: 
#       Sum of numbers:  5
#       Sum of numbers:  28
#       Sum of numbers:  326
