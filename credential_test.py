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
if __name__ == '__main__':
    unittest.main()
