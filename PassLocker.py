#!/usr/bin/env python3.8
from credential import UserCredential
from user import User


def create_user(userName, passcode):
    """
    Function to create a new user account
    """

    new_user = User(userName, passcode)
    return new_user


def create_credential(accType, loginName, LoginPassword):
    """
    Function to create a new credential
    """
    new_credential = UserCredential(accType, loginName, LoginPassword)
    return new_credential


def save_user(user):
    """
    Function to save user account
    """
    user.save_user()


def save_credential(credential):
    """
    Function to save user credential
    """
    credential.save_credential()


def del_user(user):
    """
    Function to delete a user account or credentials
    """
    user.save_user()


def del_credential(credential):
    """
    Function to save credential
    """
    credential.save_credential()


def check_existing_user(username):
    """
    Function that check if a user exists with that username and
    returns a Boolean
    """
    return User.user_exist(username)


def check_existing_credential(username):
    """
    Function that check if a user exists with that username and
    returns a Boolean
    """
    return UserCredential.credential_exists(username)


def display_users():
    """
    Returns all the saved users available
    """
    return User.display_users()


def display_credentials():
    """
    Return all the saved users credentials available
    """
    return UserCredential.display_credentials()


def find_credential(username):
    """
    Function that finds a usercredential by login name and returns the credential
    """
    return UserCredential.find_by_username(username)


def copy_password():
    """
    Function that copies a user password
    """
    return UserCredential.copy_password()


"""Main function starts here"""


def main():
    print(
        "Welcome to Password Locker, Where you can safely store your accounts and passwords. \n What would you like to do?"
    )
    print("\n")

    while True:
        print(
            "Use these short codes for navigation: \n -> su to sign up for an account \n -> lg to Login to you account \n -> lo to log out of your account"
        )
        short_code = input().lower()
        print("\n")
        if short_code == "su":
            print("Creating New user account")
            print("-" * 10)

            print("Enter Username")
            userName = input()

            print("Create Password")
            created_passcode = input()

            print("Confirm Password")
            confirmed_passcode = input()

            while confirmed_passcode != created_passcode:
                print("Invalid Input! Password did not match!! \n Enter password again")
                created_passcode = input()
                print("Confirm password")
                confirmed_passcode = input()
                passcode = confirmed_passcode

            else:
                save_user(
                    create_user(userName, passcode)
                )
                print(f"Account creation for {userName} successful. \n Proceed to login. \n")


if __name__ == "__main__":
    main()
