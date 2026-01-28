def find_smallest(arr):
    if not arr:  
        return None
    min_value = arr[0]  
    for num in arr:
        if num < min_value:
            min_value = num  
    return min_value
numbers = [10, 25, 56, 89, 12, 34]
print("smallest element:", find_smallest(numbers))


#output: Smallest element: 10
