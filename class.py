#write a phython class bankaccount with attributes:account_number,balance,date_of_opening,customer_name.methods:deposit,withdraw,check_balance.
class BankAccount:
    account_number=input("Acc no.:")#string as we cant perform any arthematic operations.same for phone number
    balance=float(input("balance:"))
    date_of_opening=input("date of opening:")
    customer_name=input("customer name:")
    deposit=int(input("deposit:"))
    balance+=deposit
    withdraw=float(input("withdraw:"))
    check_balance=(balance+deposit)-withdraw
object1=BankAccount()
print("Account number:",object1.account_number)
print("Balance:",object1.balance)
print("Date_of_opening:",object1.date_of_opening)
print("Customer_name:",object1.customer_name)
if(object1.balance >= object1.withdraw):
   print("Available balance:",object1.check_balance)
else:
    print("insufficient balance! Available balance",object1.balance)
