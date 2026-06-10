#Check Palindrome Number
num = 151
temp = num
rev = 0

while temp > 0:
    dig = temp % 10
    rev = rev * 10 + dig
    temp //= 10

if num == rev:
    print("palindrome")
else:
    print("Not palindrome")
    
