def second_largest(array):
    newlist = []
    for i in range(len(array)):
        for j in range(len(array) - 1):
            if array[j] < array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    for i in array:
        if i not in newlist:
            newlist.append(i)
    if len(newlist) < 2:
        return None
    return newlist[1]

ans = second_largest([11, 22, 44, 55, 11])
print("the largest array : ",ans)


#Output: the largest array :  44
