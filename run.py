
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
    print(" Welcome to password_locker system . '\n' create  use-name")
    user_name = input()

    print(f" {user_name}.")
    print('\n')
    print("Enter password  you want to use")
    password= input()
    print(f"{password}.")
    print(f" this is new user_name and password created '\n'user_name is:{user_name} and password is:{password}")
    print('\n')
    print(" Create account for social media' '\n'Enter name of social media Account you want to create")
    Account = input()

    print(f" {Account}.")
    print('\n')
    print("Enter your user_name")
    user_name= input()
    print(f"{user_name}.")
    print('\n')
    print("Enter your password")
    password= input()
    print(f"{password}.")
    print('\n')
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')
    while True:
                print("Use these short codes : cA - create a new Account, dA - display Account, fA -find a Account, ex -exit the Credential list ")

                short_code = input().lower()
                if short_code == 'cA':
                            print("New Credential")
                            # print("-"Account)

                            print ("Account ....")
                            Account = input()

                            print("user_name ...")
                            user_name = input()

                            print("password ....well what would want to do")
                            password = input()
                            print(f"well {user_name}. what would you like to do?")
                            print('\n')
                            
                            password = input()
    #                         save_Credentials(create_Credential(Account,user_name,password)) # create and save Credential.
    #                         print ('\n')
    #                         print(f"New Credential  Account created is: {Account} ")
    #                         print ('\n')
    #                         save_Credentials(create_Credential(Account,user_name,password)) # create and save new contact.
    #                         print ('\n')
    #                         print(f"New Credential {Account}  created")
    #                         print ('\n')
    #             elif short_code == 'dA':

    #                     if display_Credentials():
    #                                 print("Here is a list of all your Credentials")
    #                                 print('\n')
    #                     else:
    #                                 print('\n')
    #                                 print("You dont seem to have any Credential saved yet")
    #                                 print('\n')

    #             elif  short_code == 'fc':

    #                                 print("Enter the Account you want to search for")

    #                                 search_Account = input()

    #         if check_existing_Accounts (search_Account):
    #                                 search_Account = find_by_Account(search_Account)
    #                                 print(f"{search_Credential.Account}")
    #                                 print('-' * 20)
    #                                 print(f"user_name.......{search_Credential.user_name}")
    #                                 print(f"password.......{search_Credential.password}")
    #     else:
    #                                 print("That Account does not exist")
    #         elif short_code == "ex":
    #                         print("thank you .......")
    # break
    #                            else:
    #                         print("I really didn't get that. Please use the short codes")

                            



    
if __name__ == '__main__':
    main()