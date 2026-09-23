class Account:
	next_account_number = 100001 
	
	def __init__(self, name, bal):
		self.name = name
		self.ac_num = Account.next_account_number
		Account.next_account_number += 1 
		self.bal = bal

	def deposit_money(self):
		dp_mon = (input("Please enter the deposit amount: "))
		dp_mon_int = int(dp_mon)
		self.bal += dp_mon_int

	def display_ac_details(self):
		print("Name: ", self.name)
		print("Account Number: ", self.ac_num)
		print("Initail Balance: ", self.bal)
		print("Final Balance: ", self.bal)


class CurrentAccount(Account):
	
	def withdrawal_money(self):
		wid_mon = (input("Please enter the withdrwal amount: "))
		wid_mon_int = int(wid_mon)

		if (wid_mon_int > self.bal):
			print("Insufficient Money")
		else:
		     self.bal -= wid_mon_int
		     print("Balance after withdrawal: ",self.bal)
		
		
p1 = CurrentAccount("John", 5000)

p1.deposit_money()
p1.display_ac_details()
p1.withdrawal_money()

