# Parking Lot Management System

A simple command-line parking lot management system that allows users to create accounts, log in, and manage parking operations.

## Description

This is a basic parking lot management system implemented in Python. The program enables users to:
- Create a new account
- Log in with existing credentials
- Park vehicles
- Remove vehicles
- View parking lot status
- Exit the program

The system uses dictionaries to store user information and lists to track parking lot data.

## Features

- **User Account Management**: Create new accounts with username and password (minimum 5 characters)
- **User Authentication**: Secure login system for registered users
- **Parking Management**: 
  - Park vehicles with plate numbers
  - Remove parked vehicles
  - View current parking lot status
- **Menu-Driven Interface**: Simple numbered menu options for easy navigation

## Installation

1. Clone this repository or download the source code
2. Ensure you have Python 3.x installed on your system
3. No additional dependencies required - uses only Python standard library

## Usage

1. Run the program:
   ```bash
   python parking_system.py
   ```

2. Follow the on-screen menu options:
   - **Option 1**: Create a new account
   - **Option 2**: Log in to existing account
   - **Option 3**: Exit the program

3. After logging in, you can:
   - Park a vehicle
   - Remove a vehicle
   - View parking lot status
   - Logout

## Functions

- `welcome_message()`: Displays the main menu and handles initial user input
- `option_1()`: Handles new account creation with password validation
- `user_exists()`: Checks if a username already exists in the database
- `option_2()`: Manages user login functionality
- `option_3()`: Handles program exit

## File Structure

```
parking-lot-system/
│
├── parking_system.py    # Main program file
└── README.md           # This documentation file
```

## Example Usage

```
=== PARKING LOT MANAGEMENT SYSTEM ===

welcome to the mall, kindly select an option:
1 - create an account
2 - log in
3 - exit
> 1

enter your name: JohnDoe
enter your five character password: password123
Account creation successful...
Hi JohnDoe, Account has been created for you, you are now able to log in with your credentials
```

## Requirements

- Python 3.x
- No external libraries required

## Contributing

Feel free to fork this project and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available for educational purposes.

## Future Enhancements

Potential features that could be added:
- Password encryption for better security
- Database integration for persistent storage
- Parking fee calculation
- Vehicle type classification
- Parking spot availability tracking
- Admin dashboard
