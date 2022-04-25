import unittest  # Import the unittest module
from user import User  # Import our User class


class TestUser(unittest.TestCase):
    """
    Test class that define test cases for the user class behaviors,

    Args:
        unittest.TestCase: TestCase class that aid in creating test cases.
    """

    def tearDown(self):
        """
        tearDown method to clean up after each test case has run.
        """
        User.user_list = []

    def setUp(self):
        """
        Set up method to be run before each test cases.
        """
        self.new_user = User("Joe", "123456")  # Create a user object

    def test_init(self):
        """
        test_case to test if our object is initialized properly.
        """

        self.assertEqual(self.new_user.username, "Joe")
        self.assertEqual(self.new_user.password, "123456")

    def test_save_user(self):
        '''
        test_save_user test case to test if a user is saved into the user_list
        '''
        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)