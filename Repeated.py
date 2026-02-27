print("Enter numnber and digit: ")
num,digit=(map(int,input().split()))
count=0
while num > 0:
    r=num%10
    if r == digit:
        count+=1
    num=num//10
print(count)


#Output
#Enter numnber and digit: 
#1222 2
#3
