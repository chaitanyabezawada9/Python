def count_char_frequency(s):
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
        print(f"After '{char}': {freq}")
    return freq
input_string = "Krishna Chaitanya"
final_freq = count_char_frequency(input_string)
print("\nFinal Frequency Count:")
print(final_freq)
