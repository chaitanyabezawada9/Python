def count_vowels_consonants(s):
    vowels = set("aeiouAEIOU")
    n = len(s)
    dp = [(0, 0)] * (n + 1)  # dp[i] = (vowel_count, consonant_count) for s[0:i]
    for i in range(1, n + 1):
        v, c = dp[i - 1]
        if s[i - 1].isalpha():
            if s[i - 1] in vowels:
                dp[i] = (v + 1, c)
            else:
                dp[i] = (v, c + 1)
        else:
            dp[i] = (v, c)
    return dp[n]
# Example
s = "Hello World!"
vowels, consonants = count_vowels_consonants(s)
print("Vowels:", vowels)
print("Consonants:", consonants)
