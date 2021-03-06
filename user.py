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

    def delete_user(self):
        """
        method to delete a saved user from the user_list
        """
        User.user_list.remove(self)

    @classmethod
    def user_exist(cls, username):
        """
        Method to check if a user exists from the user list.
        Args:
            username: to search if a user exists
        Returns :
            Boolean : True or false depending if the user exists
        """
        for user in cls.user_list:
            if user.user_name == username:
                return True
        return False

    @classmethod
    def display_users(cls):
        """
        method that lists available users
        """
        return cls.user_list

    # @classmethod
    # def verify_user(cls, user_name, password):
    #     """
    #         Method that verifies whether the username and
    #     password entered match with which are in the user_list
    #     """
    #     inSession_user = ""
    #     for user in User.user_list:
    #         if user.user_name == user_name and user.password == password:
    #             inSession_user = user.user_name
    #         return inSession_user
