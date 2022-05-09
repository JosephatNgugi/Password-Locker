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


def password_generate():
    """
    Generate a password for the user.
    """
    return UserCredential.password_generator()

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
                print("Oops! Password did not match!! \n Enter password again")
                created_passcode = input()
                print("Confirm password")
                confirmed_passcode = input()

            else:
                passcode = confirmed_passcode

                save_user(create_user(userName, passcode))
                print(
                    f"Account creation for {userName} was successful. \n Proceed to login. \n"
                )

            #     print("Enter Username")
            #     entered_username = input()
            #     print("Enter password")
            #     entered_password = input()

            # if entered_username != userName or entered_password != passcode:
            #     print("Invalid username or password! Try again")
            #     print("Your Username")
            #     entered_username = input()
            #     print("Your password")
            #     entered_password = input()
            # else:
            #     print(f"Hello {userName}, You're now logged in. \n")
            #     print("You can now securely save your credentials with Password Locker")

        # Check back later for more functionality
        elif short_code == "lg":
            print("Welcome, Enter your account Username.")

            userName = input()
            if check_existing_user(userName):
                print("Enter password")
                entered_passcode = input()
                while entered_passcode != passcode:
                    print("Wrong Password!! Try again! \n Password")
                    entered_passcode = input()

                else:
                    print(f"Hello {userName}, You're now logged in. \n")
                    print(
                        "You can now securely save your credentials with Password Locker. \n"
                    )
                    print(
                        "Use these Short Codes:\n -> sc to save your existing credential \n -> cc to create new credential \n -> fc to search for a credential \n -> dc to display all your saved credentials \n -> cp to copy password \n -> del to delete a credential"
                    )
                    print("\n")

                    short_code = input().lower()
                    print("\n")
                    if short_code == "sc":
                        print("Save a user Credential")
                        print("-" * 10)

                        print("Account Type e.g Facebook")
                        accType = input()

                        print("Login name")
                        loginName = input()

                        print("Login Password")
                        loginPassword = input()

                        save_credential(
                            create_credential(accType, loginName, loginPassword)
                        )  # Create and save new credential
                    elif short_code == "cc":
                        print("Creating a new user credential")
                        print("\n")

                        print("Which type of account would you like to create credentials for?")
                        accType = input()

                        print("Please enter your preffered account username")
                        loginName = input()

                        print("Would You like to auto Generate a password? \n Reply with 'yes' to auto generate a password and 'no' to manually create a password.")
                        if input().lower() == "yes":
                            print("A 9 character password of alpha numerics and symbols will be generated for you.")
                            loginPassword = password_generate()
                            print(f"Your generated password is '{loginPassword}'.\n {loginName} for {accType} credentials have been created and saved")
                            print("\n")
                            
                        elif input().lower() == "no":
                            print("Create a Password. \n HINT! Use a combination of alpha numerics and symbols for a stronger password.")
                            loginPassword = input("Your Password: ")
                            save_credential(
                            create_credential(accType, loginName, loginPassword)
                        )  # Create and save new credential
                            print(f"Your {accType} credentials with username {loginName} has been saved.")
                        
                        else:
                            print("Something isn't Right, Try Again")
                    elif short_code == "fc":
                        print("Lets Find your Credential")
                        print("\n")
                        
                        print("Enter the username of the account you would like to find credentials for.")
                        search_username = input()
                        while check_existing_credential(search_username):
                            found_credential = find_credential(search_username)
                            print(f"We found credentials for {found_credential.type} with the username {found_credential.username}")
                            print("-" *20)
                            
                            print(f"Your password is {found_credential.password}")
                        
                        else:
                            print("No credentials with that username was found..")

                                   

            else:
                print("Sorry! No account with that username was found.")


# accType, loginName, LoginPassword

if __name__ == "__main__":
    main()
