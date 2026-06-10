#Armstrong Number
num = 153
temp = num
sum = 0

while temp > 0:
    dig = temp % 10
    sum += dig ** 3
    temp //= 10

if temp == sum:
    print("Armstrong number")
else:
    print("Not Armstrong number")


