'''

amount = int(input(" Enter any Amount: "))

balance = 10000
note_allowed = 1000


if amount > 0 and amount <= balance and amount % note_allowed == 0:
	elif amount > balance:
		print("Insufficient funds")
else:
	balance -= amount
	print("Transaction Allowed")
	print(f"New Balance After Transaction, {balance}."
'''


# ATM Withdrawal Program

# Initial balance
balance = 10000 

# Prompt user for withdrawal amount
amount = int(input("Enter the amount to withdraw: "))

# First, check if the amount is valid
if amount <= 0 or amount % 1000 != 0:
    print("Invalid amount.")
elif amount > balance:
    print("Insufficient funds.")
else:
    balance -= amount
    print("Transaction Approved.")
    print(f"New balance: {balance}")

