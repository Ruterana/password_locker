
import unittest # Importing the unittest module
from user_account import Account 

class TestAccount(unittest.TestCase):



    '''
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_Account = Account("charlene","pass12!@") # create Account object

    def tearDown(self):
        '''
        test_init test case to test if the object is initialized properly
        ''' 
        Account.user_account_list=[]
    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_Account.user_name,"charlene")
        self.assertEqual(self.new_Account.password,"pass12!@")
#########test2###############
    # def test_save_Account(self):
    #     '''
    #     test_save_Account test case to test if the Account object is saved into
    #      the Account list
    #     '''
    #     self.new_Account.save_Account() # saving the new Account
    #     self.assertEqual(len(Account.Account_list),1)


if __name__ == '__main__':
    unittest.main()