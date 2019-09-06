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
if __name__ == '__main__':
    unittest.main()