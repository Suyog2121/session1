#Count Digits in a Number
num = 1234
count = 0

while num > 0:
    count += 1
    num //= 10

print("digits: ",count)
