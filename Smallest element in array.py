import math

def small(arr):
    m = math.inf
    for i in arr:
        if i < m:
            m = i
    return m

print(small([10, 4, 2, 11, 1]))


#Output: 1
