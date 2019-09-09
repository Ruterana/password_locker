class User:
    """
    Class that generates new instances of Users.
    """

    User_list = [] # Empty User list

    def __init__(self,user_name,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.password = password
    def save_User(self):

        '''
        save_User method saves User objects into User_list
        '''

        User.User_list.append(self)
    


    @classmethod
    def find_by_userpass(cls, username_search, password_search):
        '''
        Method that takes in a username/password and authenticates the user matching.
        
        '''

        for user in cls.User_list:
            if User.user_name == username_search and User.password == password_search:
                return user



    # @classmethod
    # def Existing_User(cls,user_name,password):
    #     '''
    #     method that checks if the name and password entered match entries in the users_list
    #     '''
    # Existing_user= ''
    # for User in User.User_list:
    #     if (User .user_name == user_name and password == password):
    #         Existing_user = user . user_name
    # return Existing_user
    # self.assertEqual(Existing_user, User.check_User(user2.password, user2.user_name))