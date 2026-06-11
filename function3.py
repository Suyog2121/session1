balance = 10000

def deposit():
    global balance
    amount = 5000
    balance += amount
    print("Deposited Amount:", amount)
    print("Balance:", balance)

def withdraw():
    global balance
    amount = 2000
    balance -= amount
    print("Withdrawn Amount:", amount)
    print("Balance:", balance)

deposit()
withdraw()
