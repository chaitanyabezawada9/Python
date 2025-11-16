def remove_spaces_dp(s):
    n = len(s)
    dp = [""] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] != " ":
            dp[i] = dp[i - 1] + s[i - 1]
        else:
            dp[i] = dp[i - 1]
    return dp[n]
# Example
print(remove_spaces_dp("Hello World !"))  # Output: "HelloWorld!"
