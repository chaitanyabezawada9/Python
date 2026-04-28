def inversion(arr):
    ans = 0
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                ans += 1
    return ans


array = [6, 3, 5, 2, 7]
print("There are", inversion(array), "possible inversion")