amount = int(input(" Enter any Amount: "))

balance = 10000
note_allowed = 1000


if amount <= balance and amount % note_allowed == 0:
	print("Transaction Allowed")
else:
	print("Insufficient funds or Invalid Amount")
