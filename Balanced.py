print("Enter string: ")
s=input()
open=0
close=0
for ch in s:
    if ch == '(':
        open+=1
    else:
        close+=1
if open==close:
    print("Balanced")
else:
    print("Not Balanced")

#Output:
#Enter string: 
#(()())
#Balanced
