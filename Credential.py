class Credential:
    """
    Class that generates new instances of Credentials .
    """

    Credential_list = [] # Empty User list
    
    @classmethod
    def check_User(cls,user_name,password):
    '''
    method that checks if the name and password entered math entries in the users_list
    '''
    Existing_user= ''
    for user in Credential.Credential_list:
        if (User .user_name == user_name and password == password):
            Existing_user = user . user_name
            return Existing_user
    def __init__(self,Account,user_name,password):

      # docstring removed for simplicity

        self.Account= Account
        self.user_name = user_name
        self.password = password
    def save_Credential(self):

        '''
        save_Credential method saves Credential objects into Credential_list
        '''

        Credential.Credential_list.append(self)
    
    def delete_Credential(self):

        '''
        delete_Credential method deletes a saved Credential from the Credential_list
        '''

        Credential.Credential_list.remove(self)
    @classmethod
    def find_by_Account(cls,Account):
        '''
        Method that takes in a credential  and returns a account that matches that account .

        Args:
            Account: Account to search for
        Returns :
            Credential of Account that matches the Account.
        '''

        for Credential in cls.Credential_list:
            if Credential.Account == Account:
                return Credential
    @classmethod
    def Credential_exist(cls,Account):
        '''
        Method that checks if a Account exists from the Credential list.
        Args:
            Account: ACCOUNT to search if it exists
        Returns :
            Boolean: True or false depending if the Account exists
        '''
        for Credential in cls.Credential_list:
            if Credential.Account == Account:
                    return True

        return False
    @classmethod
    def display_Credential(cls):
        '''
        method that returns the Credential list
        '''
        return cls.Credential_list