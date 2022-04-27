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