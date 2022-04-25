class User:
    """Class that generates new instances of users"""

    user_list = []  # Empty user list

    def __init__(self, username, password):
        """
        __init__ method to help us define properties for our user
        Args:
            username: new user username.
            password: new user password.
        """
    def save_user(self):
        '''
        method that saves user objects into user_list
        '''
        User.user_list.append(self)