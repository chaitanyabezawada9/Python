arr = [10, 20, 40, 30, 50, 20, 10, 20]
dict = {}
lis = []
for i in range(len(arr)):
    if arr[i] in dict:
        lis.append(arr[i])
        res = set(lis)
    else:
        dict[arr[i]]=1

print(res)



#Output: {10, 20}
