from datetime import datetime


def customer_menu_pavillion(customer_menu_selection):
    """this function displays the options available to the user (customer) after they have logged in and selected Pavillion Mall"""
    entry_time = {}
    exit_time = {}
    if customer_menu_selection == 1:
        entry_time = datetime.now()
    elif customer_menu_selection == 2:
        exit_time = datetime.now()
        duration = exit_time - entry_time
        fee = 15
        print(
            f"Your parking fee is R{fee} from {entry_time} to {exit_time}. Time in mall: {duration}")

        if entry_time is None:
            print(
                "You have not entered the parking lot yet. Please select the vehicle entry option first.")
            customer_menu_pavillion()
