num = int(input("Enter a number: ")) 

print(f"Factors of {num} is :", end=" ") 
for i in range(1, num+1):
    if num % i == 0:
        print(i, end=",")

#input:    Enter a number: 4

#output:    Factors of 4 is : 1,2,4,

