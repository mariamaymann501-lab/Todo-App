Todo App

A simple Todo List web application built with Flask and MySQL.

Features

* User registration and login
* Password hashing using bcrypt
* User-specific todo lists
* Add, edit, delete, and mark tasks as done
* Logout
* Server-side input validation
* Parameterized SQL queries

Technologies Used

* Python
* Flask
* MySQL
* MySQL Connector/Python
* bcrypt
* python-dotenv
* HTML

Requirements

* Python
* MySQL Server
* MySQL Workbench

Setup Instructions

1. Clone or download the project.
2. Create a virtual environment:
    python -m venv .venv
3. Activate the virtual environment:
    Windows PowerShell: .\.venv\Scripts\Activate.ps1
4. Install the required packages:
    python -m pip install flask mysql-connector-python bcrypt python-dotenv
5. Create the database and tables using database/schema.sql in MySQL Workbench. Create the registration database first and select it before running the schema.
6. Copy .env.example to .env and update the MySQL settings and secret key.
7. Run the application:
    python app.py
8. Open http://127.0.0.1:5000 in your browser.

Security Notes

* Passwords are hashed using bcrypt.
* SQL queries use parameters.
* Database credentials are stored in .env, which should not be committed to Git.