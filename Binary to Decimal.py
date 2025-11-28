binary=input()
b=binary[::-1]
decimal=0
for i in range(len(binary)):
    decimal=decimal+int(b[i])*(2**i)
print(decimal)


#output: 10
#        2
