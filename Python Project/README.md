# Bank Management System

<p align="center">
  A console-based Bank Management System developed to practice Python Object-Oriented Programming, inheritance, method overriding, polymorphism, modules, packages, and separation of responsibilities.
</p>

---

# About The Project

This project is a small console-based Bank Management System developed as a practical implementation of Python OOP concepts.

The application allows a user to create a savings account, add money, withdraw money, calculate interest, and view the final account summary.

The project is organized into multiple Python modules inside a package instead of keeping the complete application in a single file.

The main purpose is to demonstrate how **OOP concepts, modular programming, and basic software structure** can work together in a practical application.

---

# Features

- Create a Savings Account
- Take account information through user input
- Display current balance
- Add money to the account
- Withdraw money from the account
- Prevent withdrawal when the balance is insufficient
- Calculate interest based on the current balance
- Calculate total balance including interest
- Display a final account summary
- Use inheritance between account classes
- Use `super()` to initialize the parent class
- Use a protected-style `_balance` attribute
- Override parent methods in the child class
- Use getter method to access the balance
- Demonstrate polymorphism
- Organize the application using modules and packages

---

# Project Architecture

The application separates **input/control, business logic, and display responsibilities**.

```text
                         main.py
                            │
                     Input + Control
                            │
                            ↓
                    SavingsAccount
                            │
                     inherits from
                            ↓
                         Account
                            │
          ┌─────────────────┼─────────────────┐
          ↓                 ↓                 ↓
     add_money()      withdraw_money()   get_balance()
          │                 │                 │
          └─────────────────┼─────────────────┘
                            │
                            ↓
                    SavingsAccount
                            │
              ┌─────────────┼─────────────┐
              ↓             ↓             ↓
        Interest       Total Balance   Overridden
       Calculation      Calculation     Methods
              │             │             │
              └─────────────┼─────────────┘
                            ↓
                       AccountShow
                            │
                            ↓
                       Display Only
                            │
                            ↓
                          Output
```

### Component Responsibilities

| Component        | Responsibility                                                                 |
| ---------------- | ------------------------------------------------------------------------------ |
| `main.py`        | Takes user input, creates objects, and controls program flow                   |
| `Account`        | Provides common account data and basic account operations                      |
| `SavingsAccount` | Extends `Account` with savings-specific calculations and overridden operations |
| `AccountShow`    | Displays current and final account information                                 |
| `bank`           | Package containing the application's modules                                   |

---

# OOP Implementation

## Account — Parent Class

`Account` contains the common properties and operations that can be shared by different account types.

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

    def get_balance(self):
        return self._balance
```

### Responsibilities

- Store account holder name
- Store account balance
- Add money
- Withdraw money
- Provide balance through a getter method

---

# SavingsAccount — Child Class

`SavingsAccount` inherits from `Account` and adds savings-specific behavior.

```python
class SavingsAccount(Account):

    def __init__(self, name, balance, interest):
        super().__init__(name, balance)
        self.interest = interest
```

The class adds:

- Interest rate
- Interest calculation
- Total balance calculation
- Overridden `add_money()`
- Overridden `withdraw_money()`

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

`SavingsAccount` reuses the common functionality of `Account` instead of implementing everything again.

The child class uses:

```python
super().__init__(name, balance)
```

to call the constructor of the parent class.

This allows `Account` to initialize:

```text
name
_balance
```

while `SavingsAccount` initializes:

```text
interest
```

---

# Protected-Style Attribute

The account balance is stored as:

```python
self._balance
```

The leading underscore follows Python's protected-style naming convention.

It indicates that `_balance` is intended for internal use and can also be accessed by subclasses.

The balance is exposed through a getter:

```python
def get_balance(self):
    return self._balance
```

This avoids directly accessing `_balance` from the main application when retrieving the current balance.

---

# Method Overriding

`SavingsAccount` overrides the `add_money()` and `withdraw_money()` methods inherited from `Account`.

### Parent

```python
def add_money(self, amount):
    self._balance += amount
```

### Child

```python
def add_money(self, amount):
    self._balance += amount
```

The child class provides its own implementation of the inherited methods.

The same approach is used for:

```python
withdraw_money()
```

This demonstrates **method overriding**.

---

# Interest Calculation

The savings-specific interest calculation is implemented inside `SavingsAccount`.

```python
def calculate_interest(self):
    return self._balance * self.interest / 100
```

For example:

```text
Current Balance = 9000
Interest Rate   = 5%

Interest = 9000 × 5 / 100
         = 450
```

The final balance including interest is calculated using:

```python
def calculate_total_balance(self):
    return self._balance + self.calculate_interest()
```

Therefore:

```text
Current Balance = 9000
Interest        = 450

Total Balance   = 9450
```

All savings-related calculations remain inside `SavingsAccount`.

---

# Polymorphism

The project demonstrates polymorphism through overridden methods.

`SavingsAccount` is treated as an `Account`, while providing its own implementations of inherited methods such as:

```python
add_money()
withdraw_money()
```

The same method interface can therefore behave according to the implementation provided by the actual object.

For example:

```python
account.add_money(amount)
```

can use the implementation defined by `SavingsAccount`.

This demonstrates how a child class can provide specialized behavior while maintaining the interface inherited from its parent.

---

# Display Responsibility

The `AccountShow` class is responsible only for displaying information.

```python
class AccountShow:

    def show_current(self, account):
        print("Current Balance:", account.get_balance())

    def show_final(self, account):
        print("----- Final Account Summary -----")
        print("Name:", account.name)
        print("Current Balance:", account.get_balance())
        print("Interest Rate:", account.interest, "%")
        print("Interest Amount:", account.calculate_interest())
        print("Total Balance with Interest:", account.calculate_total_balance())
```

The important design decision is:

```text
SavingsAccount
      ↓
Calculates

AccountShow
      ↓
Displays
```

`AccountShow` does not perform the calculations itself. It calls methods from `SavingsAccount` and displays their results.

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

Contains the parent `Account` class and common account operations.

### `savings.py`

Contains the child `SavingsAccount` class, including savings-specific calculations and overridden methods.

### `show.py`

Contains the `AccountShow` class responsible for displaying account information.

### `__init__.py`

Exports the main classes from the package:

```python
from .account import Account
from .savings import SavingsAccount
from .show import AccountShow
```

This allows `main.py` to import the required classes directly from the package:

```python
from bank import SavingsAccount, AccountShow
```

---

# Project Structure

```text
Python Project/
│
├── README.md
│
└── Bank System/
    │
    ├── main.py
    │
    └── bank/
        ├── __init__.py
        ├── account.py
        ├── savings.py
        └── show.py
```

---

# Program Flow

The application follows this sequence:

```text
User
 │
 │ enters name, balance, interest rate
 ↓
main.py
 │
 │ creates SavingsAccount object
 ↓
Initial Current Balance
 │
 ↓
Add Money
 │
 ↓
Updated Current Balance
 │
 ↓
Withdraw Money
 │
 ↓
Updated Current Balance
 │
 ↓
Final Account Summary
 │
 ├── Name
 ├── Current Balance
 ├── Interest Rate
 ├── Interest Amount
 └── Total Balance with Interest
```

---

# Example

### Input

```text
Enter Name: Paris
Enter Initial Balance: 10000
Enter Interest Rate: 5

Enter amount to add: 2000

Enter amount to withdraw: 3000
```

### Output

```text
Current Balance: 10000.0

Current Balance: 12000.0

Current Balance: 9000.0

----- Final Account Summary -----
Name: Paris
Current Balance: 9000.0
Interest Rate: 5.0 %
Interest Amount: 450.0
Total Balance with Interest: 9450.0
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
