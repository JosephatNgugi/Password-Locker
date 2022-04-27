import unittest  # Import the unittest module
from user import User  # Import our User class


class TestUser(unittest.TestCase):
    """
    Test class that define test cases for the user class behaviors.

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

        self.assertEqual(self.new_user.user_name, "Joe")
        self.assertEqual(self.new_user.password, "123456")

    def test_save_user(self):
        """
        test_save_user test case to test if a user is saved into the user_list
        """
        self.new_user.save_user()  # saving the new user
        self.assertEqual(len(User.user_list), 1)

    def test_save_multiple_user(self):
        """
        test to check if we can save multiple save multiple users to our user list
        """
        self.new_user.save_user()
        test_user = User("TestUser", "78910")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

    def test_delete_user(self):
        """
        method to test if we can remove a user from our user_list
        """
        self.new_user.save_user()
        test_user = User("TestUser", "78910")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

    # def test_verify_user(self):
    #     '''
	# 	Method to test whether the user verification works to login
	# 	'''
    #     self.new_user.save_user()
    #     user2 = User('test','pswd')
    #     user2.save_user()
    #     verified_user = User.verify_user()
    #     self.assertEqual(verified_user, User.verify_user())

if __name__ == "__main__":
    unittest.main()
