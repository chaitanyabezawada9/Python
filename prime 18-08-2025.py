n = int(input("num: "))
i,temp=0,0
for i in range(2,n//2):
    if n%i == 0:
        temp=1
        break
if temp == 1:
    print("given number is not prime")
else:
    print("given number is prime")

#output:
    #====== RESTART: C:/Users/my pc/OneDrive/Desktop/Python/prime 18-08-2025.py =====
#num: 13
#given number is prime
