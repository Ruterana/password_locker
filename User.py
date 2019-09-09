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
    def find_by_user_name(cls, username):
        '''
        Method that takes in a user_name and authenticates the user matching.
        
        '''

        for user in cls.User_list:
            if User.user_name == user_name:
                return user
    @classmethod
    def User_exist(cls,user_name):
        '''
        method that checks if the  Account exist from User_list
        '''
        
        for User in cls.User_list:
            if (User.password == user_name):
                return user
        return False
    @classmethod
    def display_user(cls):
        '''
        method that returns the accountlist
        '''
        return cls.User_list