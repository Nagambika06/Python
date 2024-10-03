class Account:
  def __init__(self,bal,acc):
    self.balance=bal
    self.acc_no=acc
    print(f"The balance in your account is {self.balance}")

  def debit(self,amt):
    self.balance-=amt
    print(f"Your account is debited with Rs.{amt}")
    self.get_balance()

  def credit(self,amt):
    self.balance+=amt
    print(f"Your account is credited with Rs.{amt}")
    self.get_balance()

  def get_balance(self):
    print("The balance is :",self.balance)

acc1=Account(10000,1234)
credit_amt=int(input("Enter amount you want to credit: "))
acc1.credit(credit_amt)
debit_amt=int(input("Enter amount you want to debit: "))
acc1.debit(debit_amt)
