def reverse_string_dp(s):
    n = len(s)
    
    dp = [''] * n
    for i in range(n):
        dp[n - i - 1] = s[i]
    return ''.join(dp)
input_str = "dynamic"
reversed_str = reverse_string_dp(input_str)
print("Original String:", input_str)
print("Reversed String:", reversed_str)
