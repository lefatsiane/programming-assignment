"""this is a parking lot management system that allows users to create an account, log in, and exit the program.
The program uses a list to store the user information and a dictionary to store the user credentials
The user can select an option from the menu to create an account, log in, or exit the program.
The program also includes error handling to ensure that the user enters valid information when creating an account and logging in."""
from datetime import datetime

# this list stores the user information in the format of a tuple (user_name, password, role)
user_exists = []
# this dictionary stores the user credentials in the format of {user_name: password}
password = {}
# this dictionary stores the user roles in the format of {user_name: role}
role = {}
# this variable stores the entry time of the user when they select the vehicle entry option
entry_time = None
# this variable stores the exit time of the user when they select the vehicle exit option
exit_time = None
# this variable stores the parking fee of the user when they select the vehicle exit option
fee = None
# this variable stores the duration of the user's stay in the mall when they select the vehicle exit option
duration = None
# this variable stores the payment confirmation of the user when they select the vehicle exit option
payment_confirmation = None


def option_1(user_name, password, role):
    # this function creates an account for the user and checks if the password is at least five characters long and if the role is valid
    """this checks if the password is at least five characters long and if it is,
    it adds the user to the user_exists list. If the password is not at least five characters long,
    it prints an error message and prompts the user to enter their information again."""

    user_name = input("enter your name: ")
    password = input("enter your five character password: ")
    role = input("enter your role (admin/user/customer): ")

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

    if (user_name, password, role) in user_exists:
        print(
            f"Hi {user_name}, Account has been created for you, you are now able to log in with your credentials")
        welcome_message()
    else:
        print("Account creation failed. Please try again.")
        option_2()


def option_2(user_name="", password="", role=""):
    # this function logs the user in and checks if the credentials are correct
    """this checks if the user exists in the user_exists list and if they do, it prompts them to enter their name and password.
    If the credentials are correct, it prints a welcome message. If the credentials are incorrect,
    it prints an error message and prompts the user to enter their information again."""

    if user_exists:
        user_name = input("enter your name: ")
        password = input("enter your password: ")
        role = input("enter your role (admin/user/customer): ")

        if (user_name, password, role) in user_exists:
            print(f"welcome back {user_name}")
            select_mall()
        else:
            print("invalid credentials, please try again")
            option_2()


def select_mall():
    """this function displays the options available to the us1er (customer) after they have logged in"""

    mall = int(input(
        "select a mall to park in: \n1 - Pavillion Mall (Flat rate: R15, capacity: 250) \n2 - Gateway Mall (R10/hr, capacity: 100) \n3 - LaLucia Mall (R12/hr capped at R60, capacity: 150) \n4 - Exit\n"))
    if mall == 1:
        customer_menu_pavillion(customer_menu_selection=int(input(
            "please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Exit\n")))
    elif mall == 2:
        customer_menu_gateway(customer_menu_selection=int(input(
            "please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Exit\n")))
    elif mall == 3:
        customer_menu_lalucia(customer_menu_selection=int(input(
            "please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Exit\n")))
    elif mall == 4:
        option_3()
    else:
        print("select an available option")
        select_mall()


def customer_menu_pavillion(customer_menu_selection):
   # this function displays the options available to the user (customer) after they have logged in and selected Pavillion Mall
    """this code checks if the user has selected the vehicle entry option and if they have, it records the entry time. 
    If they have selected the vehicle exit option, it records the exit time and calculates the duration of their stay and the parking fee. 
    If they have selected the vehicle history option, it displays their parking history. 
    If they have selected the exit option, it exits the program."""

    if customer_menu_selection == 1:
        global entry_time
        entry_time = datetime.now()
        type(entry_time)
        print(f"Your entry time is {entry_time}")
        customer_menu_pavillion(customer_menu_selection=int(input(
            "Welcome to Pavillion Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

    elif customer_menu_selection == 2:
        global exit_time
        global fee
        global duration
        global payment_confirmation

        exit_time = datetime.now()
        type(exit_time)
        print(f"Your exit time is {exit_time} ")
        print(
            f"Your entry time again is {entry_time} ")
        duration = exit_time - entry_time
        fee = 15
        print(
            f"Your parking fee is R{fee} from {entry_time} to {exit_time}. Time spent in mall: {duration}")
        payment_confirmation = input(
            "would you like to confirm payment? (yes/no):")
        if payment_confirmation.lower() == "yes":
            print(
                "Payment confirmed. Thank you for using our parking lot management system.")
        elif payment_confirmation.lower() == "no":
            print(
                "Payment not confirmed. Please make sure to pay your parking fee before exiting the mall.")
            customer_menu_pavillion(customer_menu_selection=int(input(
                "Welcome to Pavillion Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            customer_menu_pavillion(customer_menu_selection=int(input(
                "Welcome to Pavillion Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))
        customer_menu_pavillion(customer_menu_selection=int(input(
            "Welcome to Pavillion Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n"))
        )

    elif customer_menu_selection == 3:  # vehicle history
        if fee == "yes":
            fee = "paid"
        elif fee is None:
            fee = "unpaid (yet)"
        else:
            fee = "unpaid"

        print(
            f"entry time: {entry_time} \nexit time: {exit_time} \nduration: {duration} \nfee: R{fee}"
        )
        customer_menu_pavillion(customer_menu_selection=int(input(
            "Welcome to Pavillion Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

    elif customer_menu_selection == 4:  # payment outstanding
        payment_confirmation = input(
            "would you like to confirm payment? (yes/no):")
        if payment_confirmation.lower() == "yes":
            print(
                "Payment confirmed. Thank you for using our parking lot management system.")
        elif payment_confirmation.lower() == "no":
            print(
                "Payment not confirmed. Please make sure to pay your parking fee before exiting the mall.")
            customer_menu_pavillion(customer_menu_selection=int(input(
                "Welcome to Pavillion Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))
    elif customer_menu_selection == 5:  # exit
        print("Thank you for using our parking lot management system. Goodbye!")
        welcome_message()

    else:
        print("select an available option")
        customer_menu_pavillion(customer_menu_selection=int(input(
            "Welcome to Pavillion Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))
    return customer_menu_selection


def customer_menu_gateway(customer_menu_selection):
    """this function displays the options available to the user (customer) after they have logged in and selected Gateway Mall"""
    if customer_menu_selection == 1:
        global entry_time
        entry_time = datetime.now()
        type(entry_time)
        print(f"Your entry time is {entry_time}")
        customer_menu_gateway(customer_menu_selection=int(input(
            "Welcome to Gateway Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

    elif customer_menu_selection == 2:
        global exit_time
        global fee
        global duration
        global payment_confirmation

        exit_time = datetime.now()
        type(exit_time)
        print(f"Your exit time is {exit_time} ")
        print(
            f"Your entry time again is {entry_time} ")
        duration = exit_time - entry_time

        hourly_rate = 10
        # converts the duration from seconds to hours
        duration_parked_hours = duration.total_seconds() / 3600
        # calculates the parking fee based on the hourly rate and the duration of the user's stay in the mall
        fee = round(hourly_rate + (hourly_rate * duration_parked_hours))

        print(
            f"Your parking fee is R{fee} from {entry_time} to {exit_time}. Time spent in mall: {duration}")
        payment_confirmation = input(
            "would you like to confirm payment? (yes/no):")
        if payment_confirmation.lower() == "yes":
            print(
                "Payment confirmed. Thank you for using our parking lot management system.")
        elif payment_confirmation.lower() == "no":
            print(
                "Payment not confirmed. Please make sure to pay your parking fee before exiting the mall.")
            customer_menu_gateway(customer_menu_selection=int(input(
                "Welcome to Gateway Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            customer_menu_gateway(customer_menu_selection=int(input(
                "Welcome to Gateway Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))
        customer_menu_gateway(customer_menu_selection=int(input(
            "Welcome to Gateway Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n"))
        )

    elif customer_menu_selection == 3:  # vehicle history
        if fee == "yes":
            fee = "paid"
        elif fee is None:
            fee = "unpaid (yet)"
        else:
            fee = "unpaid"

        print(
            f"entry time: {entry_time} \nexit time: {exit_time} \nduration: {duration} \nfee: R{fee}"
        )
        customer_menu_gateway(customer_menu_selection=int(input(
            "Welcome to Gateway Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

    elif customer_menu_selection == 4:  # payment outstanding
        payment_confirmation = input(
            "would you like to confirm payment? (yes/no):")
        if payment_confirmation.lower() == "yes":
            print(
                "Payment confirmed. Thank you for using our parking lot management system.")
        elif payment_confirmation.lower() == "no":
            print(
                "Payment not confirmed. Please make sure to pay your parking fee before exiting the mall.")
            customer_menu_gateway(customer_menu_selection=int(input(
                "Welcome to Gateway Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

    elif customer_menu_selection == 5:  # exit
        print("Thank you for using our parking lot management system. Goodbye!")
        welcome_message()

    else:
        print("select an available option")
        customer_menu_gateway(customer_menu_selection=int(input(
            "Welcome to Gateway Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))
    return customer_menu_selection


def customer_menu_lalucia(customer_menu_selection):
    """this function displays the options available to the user (customer) after they have logged in and selected LaLucia Mall"""
    if customer_menu_selection == 1:
        global entry_time
        entry_time = datetime.now()
        type(entry_time)
        print(f"Your entry time is {entry_time}")
        customer_menu_lalucia(customer_menu_selection=int(input(
            "Welcome to La Lucia Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

    elif customer_menu_selection == 2:
        # this code calculates the parking fee for the user based on the duration of their stay in the mall and the hourly rate.
        # It also includes a cap on the maximum fee that can be charged. The user is then prompted to confirm payment, and if they do, a confirmation message is printed.
        # If they do not confirm payment, they are reminded to pay their parking fee before exiting the mall and are prompted to select an option from the menu again.
        global exit_time
        global fee
        global duration
        global payment_confirmation

        exit_time = datetime.now()
        type(exit_time)
        print(f"Your exit time is {exit_time} ")
        print(
            f"Your entry time again is {entry_time} ")
        duration = exit_time - entry_time

        hourly_rate = 12
        duration_parked_hours = duration.total_seconds() / 3600
        fee = round(hourly_rate + (hourly_rate * duration_parked_hours))
        if fee > 60:
            fee = 60

        print(
            f"Your parking fee is R{fee} from {entry_time} to {exit_time}. Time spent in mall: {duration}")
        payment_confirmation = input(
            "would you like to confirm payment? (yes/no):")
        if payment_confirmation.lower() == "yes":
            print(
                "Payment confirmed. Thank you for using our parking lot management system.")
        elif payment_confirmation.lower() == "no":
            print(
                "Payment not confirmed. Please make sure to pay your parking fee before exiting the mall.")
            customer_menu_lalucia(customer_menu_selection=int(input(
                "Welcome to La Lucia Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            customer_menu_lalucia(customer_menu_selection=int(input(
                "Welcome to La Lucia Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))
        customer_menu_pavillion(customer_menu_selection=int(input(
            "Welcome to Pavillion Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n"))
        )

    elif customer_menu_selection == 3:  # vehicle history
        # this code checks if the fee variable is equal to "yes" and if it is, it sets the fee variable to "paid". If the fee variable is None, it sets the fee variable to "unpaid (yet)". Otherwise, it sets the fee variable to "unpaid". Then it prints the entry time, exit time, duration, and fee for the user's parking history. Finally, it prompts the user to select an option from the menu again.
        if fee == "yes":
            fee = "paid"
        elif fee is None:
            fee = "unpaid (yet)"
        else:
            fee = "unpaid"

        print(
            f"entry time: {entry_time} \nexit time: {exit_time} \nduration: {duration} \nfee: R{fee}"
        )
        customer_menu_lalucia(customer_menu_selection=int(input(
            "Welcome to La Lucia Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

    elif customer_menu_selection == 4:  # payment outstanding
        payment_confirmation = input(
            "would you like to confirm payment? (yes/no):")
        if payment_confirmation.lower() == "yes":
            print(
                "Payment confirmed. Thank you for using our parking lot management system.")
        elif payment_confirmation.lower() == "no":
            print(
                "Payment not confirmed. Please make sure to pay your parking fee before exiting the mall.")
            customer_menu_lalucia(customer_menu_selection=int(input(
                "Welcome to La Lucia Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))

    elif customer_menu_selection == 5:  # exit
        print("Thank you for using our parking lot management system. Goodbye!")
        welcome_message()

    else:
        print("select an available option")
        customer_menu_lalucia(customer_menu_selection=int(input(
            "Welcome to La Lucia Mall! Please select an option: \n1 - Vehicle entry \n2 - Vehicle exit \n3 - vehicle history \n4 - Payment Outstanding \n5 - Exit\n")))
    return customer_menu_selection


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
