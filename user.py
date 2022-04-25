class User:
    """Class that generates new instances of users"""

    user_list = []  # Empty user list

    def __init__(self, user_name, password):
        """
        __init__ method to help us define properties for our user
        Args:
            user_name: new user username.
            password: new user password.
        """
        self.user_name = user_name
        self.password = password

    def save_user(self):
        """
        method that saves user objects into user_list
        """
        User.user_list.append(self)
