
#!/usr/bin/env python3.6
import pyperclip
from User import User
from Credential import Credential
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
#### for credentials##########
def save_Credentials(Credential):
    '''
    function to save Credential

    '''
    Credential.save_Credential
    '''
    save_Credential method saves Credential objects into Credential_list
    '''
    Credential.Credential_list.append(self)
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
                print("Use these short codes :\n cA - create a new Account,\n lg-login,\n ex-exit ")

                short_code = input().lower()
                if short_code== 'ex':
                    break
                elif short_code == 'ca':
                            
                            print("-"*30)
                            print('\n')
                            print("create new Account: ")
                            user_name = input("Enter user_name -")
                            passwor= input("Enter password -")
                            save_Users(create( user_name,password))
                            print(f" new Account created for: {user_name}. what would you like to do?")
                            print('\n')
                elif short_code == 'lg':
                           print("-"*20)
                           print('\n')
                           print('Enter your account details to login:')
                           print('\n')
                           username = input('Enter your first name - ')
                           password = str(input('Enter your password - '))
                           user_exists = verify_user(user_name,password)
                if user_exists == user_name:
                           print('\n')
                           print(f'Welcome {username}. Please select a short code to continue.')
                            
                           



    
if __name__ == '__main__':
    main()