class User:
    """
    Class that generates new instances of Users.
    """

    Use_list = [] # Empty User list

    def __init__(self,user_name,password):

      # docstring removed for simplicity

        self.user_name = user_name
        self.password = password
        