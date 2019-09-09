
#!/usr/bin/env python3.6
import pyperclip
from User import User
from Credential import Credential
import random


def create_User(user_name,password):
    '''
    Function to create a new User
    '''
    new_User = User(user_name,password)
    return new_User
def save_Users(User):
    '''
    Function to save User
    '''
    User.save_User()
def Display_User():
    '''
    function that return all saved account
    '''
    return User.display_user()


######for creating credential
def create_Credential(Account,user_name,password):
    '''
    method that create new credentials
    '''
    new_credential = Credential(Account,user_name,password)
    return new_credential

#### for credentials##########

def save_credentials(credential):
   '''
   Function to save user
   '''
   credential.save_credential()

   ######TO DISPLAY

   def display_credentials():
    '''
    function that display all saved account
    '''
    return credential.display_Credentials()



def del_Credentials(Credential):
    '''
    Function to delete a Credential
    '''
    Credential.delete_Credential()
def find_Credential(Account):
    '''
    Function that finds a Credential by Account and returns the Account
    '''
    return Credential.find_by_Account(Account)
def check_existing_Credential(Account):
    '''
    Function that check if a Account exists with that Account and return a Boolean
    '''
    return Credential.Credential_exist(Account)
def main():
    print(" Welcome to password_locker system . '\n' first select a short code  ")
    

    while True:
                print("Use these short codes :\n cA - create a new Account,\n lg-login,\n ex-exit,\n dc ")

                short_code = input().lower()
                if short_code== 'ex':
                    break
                elif short_code == 'ca':
                            
                            print("-"*30)
                            print('\n')
                            print("create new Account: ")
                            user_name = input("Enter user_name -")
                            password= input("Enter password -")
                            save_Users(create_User( user_name,password))
                            print(f" new Account created for: {user_name}. what would you like to do?")
                            print('\n')
                elif short_code == 'lg':
                           print("-"*20)
                           print('\n')
                           print('Enter your account details to login:')
                           print('\n')
                           user_name1 = input('Enter your use_name - ')
                           if user_name !=user_name : 
                               continue
                           else:

                              password1 = str(input('Enter your password - '))
                              if password1 != password :
                                continue

                              else:
                                  while True:
                                        print("-"*30)
                                        print('Our short codes: \n ac-Add existing Credential \n cc-Create a Credential \n dc-Display Credentials \n fc- Find a Credential  \n cp-Copy Password \n rc- Delete account \n ex-Exit \n g-generate' )                            
                                        print('\n')
                                        short_code = input('Enter a short_code for your choice: ').lower()
                                        print("-"*20)
                                        if short_code == 'ex':
                                            print(f'thanks {user_name}for using our app')
                                            break
                                        elif short_code == 'cc':
                                            print('Enter your account name........')
                                            Account = input()
                                            print('\n')

                                            print('Enter your account username............')
                                            user_name = input()
                                            print('\n')

                                            print('choose gen -to generate password or T -to type the password of your choice ')
                                            shortCode = input()
                                            
                                            if shortCode =='gen':
                                                passwordlen = 8
                                                s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?0123456789"
                                                pasword ="".join (random.sample(s,passwordlen))
                                                print(f'your password:{pasword}')
                                            else :
                                                print('enter your password.....')
                                            pasword = input()
                                        elif short_code == 'dc':
                                            if display_credentials():

                                                print('here is the list of your account')
                                                print('\n')

                                                for credential in display_credentials():
                                                    print(f'{credential.Account} ..........{credential.user_name} ........{credential.password1}')
                                                    print('\n')
                                            


    
if __name__ == '__main__':
     main()