class InsufficientBalance(Exception):
  pass
class BankAccount:
  def __init__(self,account_number,balance):
    self.account_number = account_number
    self.__balance=balance

  def deposit(self,amount):
    self.__balance += amount

  def withdraw(self,amount):
    if amount > self.__balance:
      raise InsufficientBalance("Insufficient Balance)
    else:
      self.__balance -= amount
	
	def check_balance(self):
		return self.__balance
account = BankAccount(77002123221,10000)
account.deposit(50000)
try:
	account.withdraw(1000)
except InsufficientBalance as e:
	print(f"Error processing your request. \n {e}")
