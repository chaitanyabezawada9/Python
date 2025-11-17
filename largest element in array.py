def find_largest(arr):
    if not arr:  
        return None
    max_value = arr[0]  
    for num in arr:
        if num > max_value:
            max_value = num  
    return max_value
numbers = [10, 25, 56, 89, 12, 34]
print("Largest element:", find_largest(numbers))
