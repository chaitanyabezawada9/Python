def is_armstrong(num):
    n=len(str(num))
    sum=0
    for digit in str(num):
        sum +=int(digit)**n
    return num==sum
num =int(input(" "))
if is_armstrong(num):
    print(f"{num} is armstrong number.")
else:
    print(f"{num} is not armstrong number.")


#input: 153
#output: 153 is armstrong number.
