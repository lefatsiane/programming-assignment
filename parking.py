"""this is a parking lot management system that allows users to create an account, log in, and exit the program. 
The program uses a list to store the user information and a dictionary to store the user credentials 
The user can select an option from the menu to create an account, log in, or exit the program.
The program also includes error handling to ensure that the user enters valid information when creating an account and logging in."""

user_exists = []
password = {}
role = {}


def option_1(user_name, password, role):
    """this function creates an account for the user"""
    user_name = input("enter your name: ")
    password = input("enter your five character password: ")
    role = input("enter your role (admin/user/customer): ")

    """this checks if the password is at least five characters long and if it is, 
    it adds the user to the user_exists list. If the password is not at least five characters long, 
    it prints an error message and prompts the user to enter their information again."""

    if len(password) >= 5:
        global user_exists
        user_exists.append((user_name, password, role))
        print("Account creation successful...")
    else:
        print("password must be at least five characters")
        option_1(user_name, password, role)

    if role != "admin" and role != "user" and role != "customer":
        print("invalid role, please enter a valid role")
        option_1(user_name, password, role)

    """this checks if the user was added to the user_exists list and if they were, 
    it prints a success message. If they were not, it prints an error message and prompts the user to enter their information again."""
    if (user_name, password, role) in user_exists:
        print(
            f"Hi {user_name}, Account has been created for you, you are now able to log in with your credentials")
        welcome_message()
    else:
        print("Account creation failed. Please try again.")
        option_2()


def option_2(user_name="", password="", role=""):
    """this function logs the user in"""

    """this checks if the user exists in the user_exists list and if they do, it prompts them to enter their name and password. 
    If the credentials are correct, it prints a welcome message. If the credentials are incorrect, 
    it prints an error message and prompts the user to enter their information again."""

    if user_exists:
        user_name = input("enter your name: ")
        password = input("enter your password: ")
        role = input("enter your role (admin/user/customer): ")

        if (user_name, password, role) in user_exists:
            print(f"welcome back {user_name}")
        else:
            print("invalid credentials, please try again")
            option_2()
    print("You are now logged in successfully!")


def option_3():
    """this function exits the program"""
    print("Thank you for using the parking lot management system. Goodbye!")
    welcome_message()


def welcome_message():
    """this function welcomes the user to the parking lot and prompts them to select an option"""

    option = int(input(
        "welcome to the mall, kindly select an option: \n1 - create an account \n2 - log in\n3 - exit\n"))
    if option == 3:
        option_3()
    elif option == 1:
        option_1(user_name="", password="", role="")
    elif option == 2:
        option_2(user_name="", password="", role="")
    else:
        print("select an available option")
        welcome_message()


welcome_message()
