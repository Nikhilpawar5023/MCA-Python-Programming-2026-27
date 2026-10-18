# P13 ATM
pin = 1234
balance = 10000
user_pin = int(input("Enter PIN: "))
if user_pin == pin:
    amount = float(input("Enter amount to withdraw: "))
    if amount <= balance:
        balance = balance - amount
        print("Withdraw Success")
        print("Remaining balance", balance)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")
