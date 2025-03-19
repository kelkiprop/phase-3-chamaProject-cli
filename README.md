# phase-3-chamaProject-cli
# Chama Management System

## Overview
The **Chama Management System** is a command-line application that allows users to manage a savings and loan group (Chama). It provides functionalities to add members, record contributions, request loans, view financial transactions, and manage loans efficiently using SQLAlchemy.

## Features
- **Member Management**: Add, view, and delete members.
- **Contribution Tracking**: Record and view contributions made by members.
- **Loan Management**: Request loans, view loan details, and update loan statuses.
- **Database Integration**: Uses SQLAlchemy ORM to interact with a SQLite database.

## Project Structure
```
Chama-Management/
│── database.py         # Database connection setup
│── models.py           # SQLAlchemy models for Member, Contribution, Loan
│── operations.py       # Main CLI application logic
│── README.md           # Project documentation
│── requirements.txt    # Project dependencies
```

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/kelkiprop/phase-3-chamaProject-cli
   cd chama-management
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
### Initialize the Database
Run the following command to set up the database:
```sh
python operations.py
```

### Available Commands
When you run `operations.py`, you will be presented with a menu:
1. Add Member
2. Add Contribution
3. Request Loan
4. View Members
5. View Contributions
6. View Loans
7. Delete Member
8. Update Loan Status
9. Exit

Follow the prompts to interact with the system.

## Database Schema
### Members Table
| Column  | Type  |
|---------|-------|
| id      | Integer (Primary Key) |
| name    | String |
| phone   | String |

### Contributions Table
| Column     | Type  |
|------------|-------|
| id         | Integer (Primary Key) |
| member_id  | Integer (Foreign Key) |
| amount     | Float  |
| date       | Date   |

### Loans Table
| Column     | Type  |
|------------|-------|
| id         | Integer (Primary Key) |
| member_id  | Integer (Foreign Key) |
| amount     | Float  |
| date       | Date   |
| status     | String (Pending/Approved/Rejected) |

## Dependencies
- Python 3.x
- SQLAlchemy

Install dependencies using:
```sh
pip install -r requirements.txt
```

## Contributing
Feel free to fork this repository and submit pull requests. Ensure your code follows PEP 8 guidelines.

## License
This project is licensed under the MIT License.

