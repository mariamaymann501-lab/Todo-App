# Todo-App
Team Members
Member 1:Mariam Ayman Ahmed -- 2304068
Designed and implemented the MySQL database schema.
Implemented user registration, login, logout, and session management.
Implemented password hashing and duplicate-email handling.
Implemented private user-specific to-do list access.
Tested authentication and database constraints.

Member 2:Jana Mohamed Deyaa -- 2304069
Implemented to-do creation, editing, completion, and deletion.
Implemented client-side and server-side validation for to-do forms.
Designed the user interface and responsive mobile layout.
Implemented delete confirmation and user feedback.
Tested to-do operations and mobile responsiveness.

Shared Responsibilities:
Reviewed and tested each other’s code.
Verified parameterized SQL queries and user-specific data access.
Prepared the README, screenshots, and final GitHub submission.
Both members contributed commits to the shared repository.
------------------
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


<img width="1600" height="880" alt="image" src="https://github.com/user-attachments/assets/37f8412b-e307-4008-9659-0000c2cb1916" />
<img width="1600" height="880" alt="WhatsApp Image 2026-10-12 at 11 32 23 PM" src="https://github.com/user-attachments/assets/444a908d-f64e-41d4-b4d3-af31a17979d0" />
<img width="905" height="731" alt="WhatsApp Image 2026-10-12 at 11 34 51 PM" src="https://github.com/user-attachments/assets/5cfd92a1-860a-44c5-9510-1bfb19f2d563" />
<img width="1222" height="638" alt="WhatsApp Image 2026-10-12 at 11 35 10 PM" src="https://github.com/user-attachments/assets/4620c0c9-08c4-4863-ade2-aa8eb4282bcf" />
