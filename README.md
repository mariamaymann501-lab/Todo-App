Todo App
Team Members :
Member 1: Mariam Ayman Ahmed -- 2304069
* Designed and implemented the MySQL database schema.
* Implemented user registration, login, logout, and session management.
* Implemented password hashing and duplicate-email handling.
* Implemented private user-specific to-do list access.
* Tested authentication and database constraints.

Member 2: Jana Mohamed Deyaa -- 2304069
* Implemented to-do creation, editing, completion, and deletion.
* Implemented client-side and server-side validation for to-do forms.
* Designed the user interface and responsive mobile layout.
* Implemented delete confirmation and user feedback.
* Tested to-do operations and mobile responsiveness.

Shared Responsibilities:
* Reviewed and tested each other’s code.
* Verified parameterized SQL queries and user-specific data access.
* Prepared the README, screenshots, and final GitHub submission.
* Both members contributed commits to the shared repository.

A simple Todo List web application built with Flask and MySQL:

Features:
* User registration and login
* Password hashing using bcrypt
* User-specific todo lists
* Add, edit, delete, and mark tasks as done
* Logout
* Server-side input validation
* Parameterized SQL queries

Technologies Used:
* Python
* Flask
* MySQL
* MySQL Connector/Python
* bcrypt
* python-dotenv
* HTML

Requirements:
* Python
* MySQL Server
* MySQL Workbench

Setup Instructions:
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

Security Notes:
* Passwords are hashed using bcrypt.
* SQL queries use parameters.
* Database credentials are stored in .env, which should not be committed to Git.

<img width="1600" height="887" alt="WhatsApp Image 2026-10-12 at 11 32 23 PM (1)" src="https://github.com/user-attachments/assets/a976d7a6-0c54-4007-a803-cb3710443a49" />
<img width="1600" height="880" alt="WhatsApp Image 2026-10-12 at 11 32 23 PM" src="https://github.com/user-attachments/assets/bb69ecce-4344-405c-b4d1-38ebe95b223c" />
<img width="905" height="731" alt="WhatsApp Image 2026-10-12 at 11 34 51 PM" src="https://github.com/user-attachments/assets/4f0dea39-c874-431e-bfb5-a0212be9dcc9" />
<img width="1222" height="638" alt="WhatsApp Image 2026-10-12 at 11 35 10 PM" src="https://github.com/user-attachments/assets/0a275043-3a10-4b63-9454-7a3913ee5459" />
<img width="1600" height="854" alt="WhatsApp Image 2026-10-12 at 11 45 01 PM" src="https://github.com/user-attachments/assets/035a5818-928e-48dc-94c9-ccd69f8d34c9" />


Database Questions:

(a) Why do UPDATE and DELETE contain AND user_id = ??
The condition ensures that a user can update or delete only their own to-dos. Without it, a user could modify or delete another user’s to-do if they know its ID.

(b) What happens if a to-do is inserted for a user_id that does not exist?
The database rejects the insertion because the user_id references a user that does not exist in the users table. This is the foreign key constraint, which enforces referential integrity.

(c) Why store a password hash instead of the password?
Storing a bcrypt hash protects users’ original passwords from being exposed directly if the database is compromised. During login, the application verifies the entered password against the stored hash.

(d) Why check for an empty name if the column is NOT NULL?
NOT NULL prevents a value from being NULL, but it still allows an empty string (''). The application must validate the name and reject empty or whitespace-only input.
