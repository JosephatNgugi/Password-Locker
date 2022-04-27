import pyperclip


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

    def delete_credential(self):
        """
        method to delete user credential from the credentials array
        """
        UserCredential.credentials.remove(self)

    @classmethod
    def display_credentials(cls):
        '''
        displays the user credentials list
        '''
        return cls.credentials

    @classmethod
    def credential_exists(cls, username):
        """
        To check if a credentials exists
        Args :
            username: username to search if it exists
        Return:
            Boolean: True or false depending whethe the credentials exist
        """

        for credential in cls.credentials:
            if credential.username == username:
                return True
        return False

    @classmethod
    def find_by_username(cls, username):
        """
        Method that takes in account type and returns credentials for the matching type .
        Args:
            type: account type to search for
        Returns:
            credentials of the account type match
        """
        for credential in cls.credentials:
            if credential.type == type:
                return credential
            elif credential.username == username:
                return credential

    @classmethod
    def copy_password(cls, username):
        ''''
        method to copy a password to clipboard
        '''
        credential_found = UserCredential.find_by_username(username)
        pyperclip.copy(credential_found.password)

