import unittest

from credentials import Credential

class TestUser(unittest.TestCase):
    '''
    Test class that defines the test cases for user class
    behaviours
    '''
    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_credential = Credential("twitter","muko12")
    def test_init(self):
        '''
        test_init checks if the object is initialised properly
        '''
        self.assertEqual(self.new_credential.account_name,"twitter")
        self.assertEqual(self.new_credential.passkey,"muko12")
    def test_save_credential(self):
        '''
        test_save_credential tests if a new credential has been added to credentials
        list of a user
        '''
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def test_display_credentials(self):
        '''
        test to display the credentials of a user
        '''
        self.assertEqual(Credential.display_credentials(),Credential.credential_list)
    def test_delete_credential(self):
        '''
        test_delete_credential to see if we can remove a 
        credential from credentials list
        '''
        self.new_credential.save_credential()
        test_credential = Credential("test","0893uhjnv")
        test_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)


if __name__ == '__main__':
    unittest.main()
