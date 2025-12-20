def getHCF(a, b):
    return b == 0 and a or getHCF(b, a % b)
num1 = 10
num2 = 28
num1 >= 0 and num1 or -num1
num2 >= 0 and num2 or -num2
print("HCF of", num1, "and", num2, "is", getHCF(num1, num2))    