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
    # def save_User(self):

    #     '''
    #     save_User method saves User objects into User_list
    #     '''

    #     User.User_list.append(self)
        