import unittest # Importing the unittest module
from User import User # Importing the User class

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the User class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_User = User("charlene","pass@!") # create User object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_User.user_name,"charlene")
        self.assertEqual(self.new_User.password,"pass@!")
#######test2#########
    def test_save_User(self):
        '''
        test_save_User test case to test if the User object is saved into
         the User list
        '''
        self.new_User.save_User() # saving the new User
        self.assertEqual(len(User.User_list),1)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.User_list = []

    def test_check_user_(self):
        '''
        Function to test whether the login in function check_user works as expected
        '''
        self.new_User = Account('charlene','charlen')
        self.new_User.save_user()
        User2 = Account('Tuyishime', 'CHAR@!#')
        User2.save_user()
        User3 = Account('Tubane', 'cha')
        User3.save()

        for User in Account.users_list:
            if User.user_name == User2.user_name and User.password == User2.password:
                current_user = user.user_name
        return current_user
        self.assertEqual(Existing_User, Credentials.check_User(user2.password, user2.user_name))

if __name__ == '__main__' :
    unittest.main()