import unittest #unnitest module import
import pyperclip
from user import User


class TestUser(unittest.TestCase):
    '''
     Test class that defines the test cases for user class
    behaviours
    '''
    def setUp(self):
        '''
        Setup method to run before each test cases
        '''
        self.new_user = User("Adrian","Etenyi","Mutemuas2001")
    def test_init(self):
        '''
        test_init checks if the object is initialised properly
        '''
        self.assertEqual(self.new_user.first_name,"Adrian")
        self.assertEqual(self.new_user.second_name,"Etenyi")
        self.assertEqual(self.new_user.password,"Mutemuas2001")

if __name__ == '__main__':
    unittest.main()
