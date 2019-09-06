import unittest # Importing the unittest module
from Credential import Credential # Importing the Credential class

class TestCredential(unittest.TestCase):

    '''
    Test class that defines test cases for the Credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Credential = Credential("Facebook","kailla","face@!3!") # create User object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_Credential.Account,"Facebook")
        self.assertEqual(self.new_Credential.user_name,"kailla")
        self.assertEqual(self.new_Credential.password,"face@!3!")
if __name__ == '__main__':
    unittest.main()