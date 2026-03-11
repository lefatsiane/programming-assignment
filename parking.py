"""this is a simple parking lot management system that allows users to create an account, log in and exit the program. The program uses a dictionary to store user information and a list to store parking lot information. The program also uses functions to handle different options for the user."""


def option_1():
    """this function creates an account for the user"""
    user_name = input("enter your name: ")
    password = input("enter your five character password: ")

    if len(password) >= 5:
        print("Account creation successful...")
    else:
        print("password must be at least five characters")
        option_1()

    print(f"Hi {user_name}, Account has been created for you, you are now able to log in with your credentials")
    user_exists()
    option_2()
    return user_name, password


def user_exists():
    """this function checks if the user exists in the database"""
    if user_name in database:
        print("you already have an account, you can log in with your credentials")
        option_2()
        return True


def option_2():
    """this function logs the user in"""
    print("you selected option 2")


def option_3():
    """this function exits the program"""
    print("you selected option 3")


def welcome_message():
    """this function welcomes the user to the parking lot and prompts them to select an option"""

    option = int(input(
        "welcome to the mall, kindly select an option: \n1 - create an account \n2 - log in\n3 - exit\n"))
    if option == 3:
        option_3()
    elif option == 1:
        option_1()
    elif option == 2:
        option_2()
    else:
        print("select an available option")
        welcome_message()


welcome_message()
