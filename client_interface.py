from openpyxl import load_workbook
import pandas as pd
from time import sleep
import random
from art import * # To print out the logo in ASCII https://pypi.org/project/art/ for Documentation

filename = "Dear_Universe/dear_universe.xlsx"
dearuni_db = load_workbook(filename)
users_db = pd.read_excel(filename, sheet_name="Users", header=0)

# Client interface - Account Creation and Account Sign-In

# Logo of the Dear_Universe app
def app_logo():
    # ASCII Logo
    tprint("Dear_Universe")

    app_menu()

# App's menu
def app_menu():
    print("1. Create account")
    print("2. Sign in")
    print("3. Quit\n")

    menu_choice()

# Choices from the App's menu
def menu_choice():
    while True:
        try:
            i = input("What is your choice ? > ")
            if i in ["1", "2", "3"]:
                # If user chooses 3, send to the Quit Program def
                if i in "3":
                    quit_program()
                # If user chooses 2, send to the Account Sign-In def
                elif i in "2":
                    user_account_signin()
                    break
                # If user chooses 1, send to the Account Creation def
                elif i in "1":
                    user_account_creation()
                    break
            else:
                raise AssertionError
        # If neither of 1, 2, 3 choices, returns an error and lets the User try again
        except AssertionError:
            print("An error has occured.\n")

# If menu_choice is 3, quits the program
def quit_program():
    quit()

# If menu_choice is 2, Account Sign-In
def user_account_signin():
    print("Welcome back !\n")
    global user_email
    user_email = input("What is your email adress ? > ")
    # Checks if the email is already in the database
    global check_email
    check_email = users_db.loc[users_db["User_Email"] == user_email].get("User_Email").to_string(index=False)
    user_password_try()

def user_password_try(attempts=3):
    while True:
        # If the email is already in the database, asks for the password
        if user_email == check_email:
            while True:
                user_password = input("What is your password ? > ")
                # Checks if the password matches the previously said email
                check_password = users_db.loc[(users_db["User_Email"] == user_email) & (users_db["User_Password"] == user_password)].get("User_Password").to_string(index=False)
                # If the password is matches the email, retrieve the matching User_ID and Welcomes the User then send to User Signed-In def
                if user_password == check_password:
                    user_name = users_db.loc[(users_db["User_Email"] == user_email) & (users_db["User_Password"] == user_password)].get("User_ID").to_string(index=False)
                    print(f"\nWelcome {user_name} ! You've successfully signed in !")
                    user_signedin()
                # If the password doesn't match the email, prints an error and asks to try again
                else:
                    # Removes 1 from the 3 beginning attempts
                    attempts += -1
                    print(f"\nSorry, the email and/or password don't match out database. Attempts: {attempts}\n")
                    # If attempts = 0, prints an error and quits the program
                    if attempts == 0:
                        print("You tried 3 wrong passwords. The application is going to close in three seconds.") ; sleep(3)
                        quit()
        # If the email is not already in the database, asks to try again
        else:
            print("Sorry, we can't find your email in our database. Please try again.\n")
            user_account_signin()

# Once the email and password match, for now quits the program
def user_signedin():
    quit()

# If menu_choice is 1, Account Creation
def user_account_creation():
    print("Welcome ! Here's a few questions so we can get started :\n")
    user_id = input("Choose an id > ")
    user_firstname = input("What is your first name ? > ")
    user_lastname = input("What is your last name ? > ")
    while True:
        user_mail = input("What is your email adress ? > ")
        # Checks if the email is already in the database
        check_usedmail = users_db.loc[users_db["User_Email"] == user_mail].get("User_Email").to_string(index=False)
        print(user_mail)
        print(check_usedmail)
        # If the email is already in the database, asks if User wants to Sign-In
        if user_mail == check_usedmail:
            while True:
                goto_signin = input("\nThis email is already used. Would you like to Sign In ? (y/n) > \n")
                # If user chooses y/Y, send to the Account Sign-In def
                if goto_signin == "y" or goto_signin == "Y":
                    user_account_signin()
                # If user chooses n/N, break the while and asks the User to put another email
                elif goto_signin == "n" or goto_signin == "N":
                    print("Please choose another email\n")
                    break
                # If user chooses neither y/Y or n/N, asks to try again
                else:
                    print("Please try again.\n")
        else:
            break

    user_password = input("Choose a password > ")
    print()

    # Adds all the User's inputs in to a new row in the database
    add = dearuni_db.active
    add_user = [[user_id, user_firstname, user_lastname, user_mail, user_password, random.randrange(0000000000, 9999999999)]]
    for row in add_user:
        add.append(row)

    # Saves the file containing the newly added row
    dearuni_db.save(filename)
    # Sends back to the App's menu
    app_menu()