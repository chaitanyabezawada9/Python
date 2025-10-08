is_strong_number = lambda num: num == sum((1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880)[int(digit)] for digit in str(num))

print(is_strong_number(145))


#output: True
