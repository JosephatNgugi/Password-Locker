import unittest  # unittest module
from credential import UserCredential  # Importing the user class


class TestCredential(unittest.TestCase):
    """
    Test class to define test cases for the UserCredential class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def tearDown(self):
        """
        tearDown method that cleans up after each test case has run
        """
        UserCredential.credentials = []

    def setUp(self):
        """
        setUp method that runs before each test case.
        """
        self.new_credential = UserCredential(
            "facebook", "name@acc.com", "2580"
        )  # Credential object

    def test_init(self):
        """
        Test if the object is initialized
        """
        self.assertEqual(self.new_credential.type, "facebook")
        self.assertEqual(self.new_credential.username, "name@acc.com")
        self.assertEqual(self.new_credential.password, "2580")

    def test_save_credential(self):
        """
        Test if a user credential object is saved to the credentials
        """
        self.new_credential.save_credential()
        self.assertEqual(len(UserCredential.credentials), 1)

    def test_save_multiple_credential(self):
        """
        test if we can save multiple credentials to the credentials array
        """
        self.new_credential.save_credential()
        test_twitterCredential = UserCredential("twitter", "0712345678", "security")
        test_twitterCredential.save_credential()
        test_instaCredential = UserCredential("instagram", "insta@now.com", "checkit")
        test_instaCredential.save_credential()
        self.assertEqual(len(UserCredential.credentials), 3)

    def test_delete_credential(self):
        """
        test if we can remove a user credential from our credentials array.
        """
        self.new_credential.save_credential()
        test_instaCredential = UserCredential("instagram", "insta@now.com", "checkit")
        test_instaCredential.save_credential()
        self.new_credential.delete_credential()  # Deleting a contact object
        self.assertEqual(len(UserCredential.credentials), 1)


if __name__ == "__main__":
    unittest.main()
