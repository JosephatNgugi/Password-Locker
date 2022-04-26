class UserCredential:
    """
    Class to generate new instances of user account credentials
    """

    credentials = []  # Empty user list

    def __init__(self, type, username, password):
        """
        an __init__ method to help use define properties for our objects.
        Args:
            type: type of account
            username: login name
            password: login password
        """
        self.type = type
        self.username = username
        self.password = password

    def save_credential(self):
        """
        method to save user credential into our credentials array
        """
        UserCredential.credentials.append(self)
