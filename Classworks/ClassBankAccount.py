class BankAccount:
	def __init__(self, account_number, account_holder_name, balance):
		self.__account_number = account_number
		self.__account_holder_name = account_holder_name
		self.__balance = balance
	
	def get_balance(self):
		return self.__balance

	def get_account_holder_name(self):
		return self.__account_holder_name

	def set_balance(self, new_balance):
		if new_balance >= 0:
			self.__balance = new_balance
		else:
			print("Error: Balance cannot be negative!")

	def deposit(self, *amounts):
		total_deposit = sum(amounts)

		if total_deposit > 0:
			self.__balance += total_deposit
			print(f"Deposited: {total_deposit}. New Balance: {self.__balance}")
		else:
			print("Deposit amount must be positive.")

	def withdraw(self, amount):

		if amount <= self.__balance:
			self.__balance -= amount
			print(f"Withdrew: {amount}. New Balance: {self.__balance}")
		else:
            		print("Error: Insufficient funds!")

	def __add__(self, other):
		combined_balance = self.__balance + other.__balance
		return combined_balance

	def __eq__(self, other):
		return self.__account_number == other.__account_number

	def __gt__(self, other):
		return self.__balance > other.__balance

	def __str__(self):
		return f"Account [{self.__account_number}] - {self.__account_holder_name}: ${self.__balance}"


account1 = BankAccount(101, "Alice", 500)
account2 = BankAccount(102, "Bob", 300)

print("--- Account Details ---")
print(account1)
print(account2)

print("\n--- Testing Deposits ---")
account1.deposit(100)         
account2.deposit(50, 75, 25)

print("\n--- Testing Withdrawals ---")
account1.withdraw(50)        
account2.withdraw(1000)

print("\n--- Testing Setter Validation ---")
print("Setting Account balance of Alice as 50")
account1.set_balance(50)
print(account1)
account2.set_balance(-50)

print("\n--- Testing Operators ---")
print(f"Combined Balance of Alice and Bob: ${account1 + account2}")
print(f"Is Account 1 the same as Account 2? {account1 == account2}")
print(f"Does Alice have more money than Bob? {account1 > account2}")




