class Credential:
    """
    Class that generates new instances of Credentials .
    """

    Credential_list = [] # Empty User list

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
        