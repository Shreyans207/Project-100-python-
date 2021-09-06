import os
import shutil
import random

disclaimer = print('Disclaimer :- This is an hypothetical game, no fraud has been made in someones account, everything is fake, it is for learning new concepts of functions in python by white hat jr.')
question = bool(input('Do you want to continue?? : '))

if (question == true) : 
    card_number =  int(input("Enter your bank card no... (account balance depends on it ;) : "))
    pin_number =  int(input("Enter your bank pin no... (account balance depends on it ;) : "))
    accountBalance = card_number/pin_number + random.randint(1000,10000)
    balance_currency = print(f'Account Balance = {acountBalance} Rs.')
    transaction = int(input("Donate Money (in rs.) : "))

    class atm : 
       def __init__(self,card_number,pin_number,transaction,accountBalance) : 
           self.card_number = card_number
           self.pin_number = pin_number
           self.transaction = transaction
           self.accountBalance = accountBalance

        def transaction(self) :
          if (self.transaction > transaction) : 
            print('YAY! Transaction completed')
            accountBalance = accountBalance - transaction
          else : 
            print(f'Sorry, Not enough money in the account.. you have only {balance_currency} in your account')
else : 
    print('Well.... Thank you :)')
    
