# Bank Management System

<p align="center">
  A console-based Bank Management System developed to practice Python Object-Oriented Programming, modular project structure, inheritance, method overriding, and polymorphism.
</p>

---

# About The Project

This project is a small console-based Bank Management System developed as a practical implementation of Python OOP concepts.

The application allows a user to create a savings account, add money, withdraw money, calculate interest, and display updated account information.

Instead of keeping the entire program in a single file, the project is divided into multiple modules and organized inside a Python package.

The main purpose of the project is to demonstrate how OOP concepts can work together in a structured, multi-file application.

---

# Features

- Create a Savings Account
- Take account information through user input
- Add money to the account
- Withdraw money from the account
- Prevent withdrawal when the balance is insufficient
- Calculate savings interest
- Display account information
- Use inheritance between account classes
- Override parent methods in the child class
- Demonstrate polymorphism
- Organize classes using modules and packages

---

# Project Architecture

```text
                         main.py
                            │
                            │
                    User Input / Object
                            │
                            ↓
                    SavingsAccount
                            │
                       inherits
                            ↓
                         Account
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
         add_money()  withdraw_money()   show()
              │             │             │
              └─────────────┼─────────────┘
                            │
                            ↓
                    SavingsAccount
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
          interest      show() override   account operations
                            │
                            ↓
                       AccountShow
                            │
                            ↓
                     account.show()
                            │
                            ↓
                       Polymorphism
```

### Component Responsibilities

| Component        | Responsibility                                               |
| ---------------- | ------------------------------------------------------------ |
| `main.py`        | Takes user input, creates objects, and controls program flow |
| `Account`        | Provides common account properties and operations            |
| `SavingsAccount` | Extends `Account` with savings-specific behavior             |
| `AccountShow`    | Handles displaying account information                       |
| `bank`           | Package containing the related modules                       |

---

# OOP Implementation

## Account — Parent Class

`Account` contains the common properties and operations shared by account types.

```python
class Account:

    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    def add_money(self, amount):
        self._balance += amount

    def withdraw_money(self, amount):
        if amount <= self._balance:
            self._balance -= amount
        else:
            print("Insufficient Balance")

    def show(self):
        print("Name:", self.name)
        print("Balance:", self._balance)
```

The class is responsible for:

- Account holder name
- Account balance
- Adding money
- Withdrawing money
- Basic account information

---

## SavingsAccount — Child Class

`SavingsAccount` inherits from `Account` and adds savings-specific functionality.

```python
class SavingsAccount(Account):

    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest
```

It extends the parent class with:

- Interest rate
- Interest calculation
- Savings-specific display
- Overridden account operations

---

# Inheritance

The project uses the following inheritance relationship:

```text
Account
   │
   │ inherits
   ↓
SavingsAccount
```

`SavingsAccount` reuses common functionality from `Account` instead of rewriting the same code.

The child class also uses:

```python
super().__init__(name, balance)
```

to initialize the parent class.

---

# Protected Attribute

The account balance is stored using:

```python
self._balance
```

The leading underscore follows Python's protected-style naming convention.

It indicates that `_balance` is intended for internal use and can also be accessed by subclasses such as `SavingsAccount`.

---

# Method Overriding & Polymorphism

The parent class defines:

```python
def show(self):
```

The child class provides its own implementation of the same method:

```python
def show(self):
```

Therefore, the same method call:

```python
account.show()
```

can execute the appropriate implementation based on the actual object.

The display helper demonstrates this behavior:

```python
class AccountShow:

    def show_account(self, account):
        account.show()
```

The `AccountShow` class does not need to know the specific account implementation. It simply calls the common `show()` interface.

This provides a simple demonstration of **polymorphic behavior**.

---

# Package & Module Structure

The project uses a dedicated Python package:

```text
bank/
│
├── __init__.py
├── account.py
├── savings.py
└── show.py
```

### `account.py`

Contains the parent `Account` class.

### `savings.py`

Contains the child `SavingsAccount` class.

### `show.py`

Contains the `AccountShow` class responsible for displaying account information.

### `__init__.py`

Exports the main classes from the package:

```python
from .account import Account
from .savings import SavingsAccount
from .show import AccountShow
```

This allows `main.py` to import the required classes directly from the package.

---

# Project Structure

```text
Bank Management System/
│
├── main.py
├── README.md
├── .gitignore
│
└── bank/
    ├── __init__.py
    ├── account.py
    ├── savings.py
    └── show.py
```

---

# Program Flow

```text
User
 │
 │ enters account information
 ↓
main.py
 │
 │ creates SavingsAccount object
 ↓
SavingsAccount
 │
 │ inherits common functionality
 ↓
Account
 │
 ├── Add Money
 ├── Withdraw Money
 └── Account Data
 │
 ↓
AccountShow
 │
 │ calls show()
 ↓
SavingsAccount.show()
 │
 ↓
Updated Account Information
```

---

# Example

### Input

```text
Enter Name: Rezwan
Enter Balance: 10000
Enter Interest: 5

Enter amount to add: 2000

Enter amount to withdraw: 3000
```

### Output

```text
Savings Account
Name: Rezwan
Balance: 10000.0
Interest: 5.0

Money added: 2000.0

Money withdrawn: 3000.0

Savings Account
Name: Rezwan
Balance: 9000.0
Interest: 5.0
```

---

# How to Run

## Prerequisites

- Python 3.x
- VS Code or any Python-supported IDE

Check Python:

```bash
python --version
```

## Run the Application

Open the project directory and run:

```bash
python main.py
```

No external Python packages are required.

---

# Technologies & Tools

| Technology      | Purpose                   |
| --------------- | ------------------------- |
| Python          | Core Programming Language |
| Python OOP      | Application Design        |
| Python Modules  | Code Separation           |
| Python Packages | Project Organization      |
| VS Code         | Development Environment   |
| Git & GitHub    | Version Control           |

---

# Author

### Rezwan Ahmed

B.Sc. Engg. in CSE Student | Aspiring Software Engineer
