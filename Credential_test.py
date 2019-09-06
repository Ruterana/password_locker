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
    def test_save_Credential(self):
        '''
        test_save_Credential test case to test if the Credential object is saved into
         the Credential list
        '''
        self.new_Credential.save_Credential() # saving the new Credential
        self.assertEqual(len(Credential.Credential_list),1)
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credential.Credential_list = []
    def test_delete_Credential(self):
            '''
            test_delete_Credential to test if we can remove a Credential from our Credential list
            '''
            self.new_Credential.save_Credential()
            test_Credential = Credential("Facebook","kailla","face@!3!") # new Credential
            test_Credential.save_Credential()

            self.new_Credential.delete_Credential()# Deleting a Credential object
            self.assertEqual(len(Credential.Credential_list),1)
if __name__ == '__main__':
    unittest.main()