import os
import shutil
import random

class atm :
   def __init__(self,card_number,pin_number,transaction,accountBalance) : 
      self.card_number = card_number
      self.pin_number = pin_number
      self.transaction = transaction
      self.accountBalance = accountBalance
      
def main() :
   disclaimer = print('Disclaimer :- This is an hypothetical game, no fraud has been made in someones account, everything is fake, it is for learning new concepts of functions in python')
   card_number =  int(input("Enter your bank card no... : "))
   pin_number =  int(input("Enter your bank pin no...  : "))
   accountBalance = 0
   print(f'Current Account Balance : {accountBalance} Rs.')
   loop = True

   accountBalance = int(input('Make deposit in your account ? : '))
   change = print('Activity Successfull')
   balance_currency = print(f'Account Balance = {accountBalance } Rs.')

   while(loop) : 
       
      transaction = int(input("Donate Money : "))

      if (accountBalance > transaction) : 
         print('YAY! Transaction completed')
         accountBalance = accountBalance - transaction
         print(f'Account Balance : {accountBalance}')

         question2 = bool(input('Wanna play more ? : '))

         if (question2 == False) : 
            loop = False
            print('Thanks for playing')
            rate = input('Rate Us : ')
         else : 
            loop = True
      else : 
         print(f'Sorry, Not enough money in the account.. you have only {accountBalance} in your account')
         accountBalance2 = accountBalance + int(input('Make deposit in your account ? : '))
         accountBalance = accountBalance2
         change2 = print('Activity Successfully')
         balance_currency = print(f'Account Balance = {accountBalance} Rs.')

if __name__ == '__main__' : 
    main()
