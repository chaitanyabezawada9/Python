print("Enter string: ")
s=input()
res=""
for i in range(len(s)):
    if s[i] not in s[0:i]:
        res+=s[i]
print(res)


#Output:
#Enter string: 
#Programming
#Progamin
