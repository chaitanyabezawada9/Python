def sum_n(n):
    total = 0
    for i in range(1, n+1):
        total+=i
    return total

num = int(input(" "))

print(f"Sum of 1 to {num} natural numbers is : {sum_n(num)}")
