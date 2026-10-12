from flask import Flask, session, render_template, request, redirect
import mysql.connector
import bcrypt
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")


def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )


@app.route("/")
def home():
    if "user_id" in session:
        return redirect("/todos")
    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    errors = {}

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")
        confirm_password = request.form.get("confirm_password", "")

        if not name:
            errors["name"] = "Name is required"

        if not email:
            errors["email"] = "Email is required"

        if not password:
            errors["password"] = "Password is required"

        if not confirm_password:
            errors["confirm_password"] = "Confirm password is required"
        elif password != confirm_password:
            errors["confirm_password"] = "Passwords do not match"

        if errors:
            return render_template("register.html", errors=errors)

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT user_id FROM users WHERE email = %s",
                (email,)
            )

            if cursor.fetchone():
                errors["email"] = "Email Already Exists"
                return render_template("register.html", errors=errors)

            password_hash = bcrypt.hashpw(
                password.encode("utf-8"),
                bcrypt.gensalt()
            ).decode("utf-8")

            cursor.execute(
                """INSERT INTO users (email, name, password_hash)
                   VALUES (%s, %s, %s)""",
                (email, name, password_hash)
            )

            db.commit()

            session["user_id"] = cursor.lastrowid
            session["name"] = name

            return redirect("/todos")

        finally:
            cursor.close()
            db.close()

    return render_template("register.html", errors=errors)


@app.route("/login", methods=["GET", "POST"])
def login():
    errors = {}

    if request.method == "POST":
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "")

        if not email:
            errors["email"] = "Email is required"

        if not password:
            errors["password"] = "Password is required"

        if errors:
            return render_template("login.html", errors=errors)

        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        try:
            cursor.execute(
                "SELECT * FROM users WHERE email = %s",
                (email,)
            )
            user = cursor.fetchone()

            if user and bcrypt.checkpw(
                password.encode("utf-8"),
                user["password_hash"].encode("utf-8")
            ):
                session["user_id"] = user["user_ID"]
                session["name"] = user["name"]
                return redirect("/todos")

            errors["general"] = "Invalid email or password"
            return render_template("login.html", errors=errors)

        finally:
            cursor.close()
            db.close()

    return render_template("login.html", errors=errors)


@app.route("/todos")
def todos():
    if "user_id" not in session:
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    try:
        cursor.execute(
            """SELECT * FROM todos
               WHERE user_id = %s
               ORDER BY created_at DESC""",
            (session["user_id"],)
        )
        tasks = cursor.fetchall()

        return render_template(
            "todos.html",
            tasks=tasks,
            session_name=session.get("name")
        )

    finally:
        cursor.close()
        db.close()


@app.route("/add", methods=["POST"])
def add_task():
    if "user_id" not in session:
        return redirect("/login")

    title = request.form.get("title", "").strip()

    error = None

    if not title:
        error = "Title is required"
    elif len(title) > 200:
        error = "Title is too long"

    if error:
        db = get_db_connection()
        cursor = db.cursor(dictionary=True)

        try:
            cursor.execute(
                """SELECT * FROM todos
                   WHERE user_id = %s
                   ORDER BY created_at DESC""",
                (session["user_id"],)
            )
            tasks = cursor.fetchall()

            return render_template(
                "todos.html",
                tasks=tasks,
                session_name=session.get("name"),
                error=error
            ), 400

        finally:
            cursor.close()
            db.close()

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            """INSERT INTO todos (user_id, title)
               VALUES (%s, %s)""",
            (session["user_id"], title)
        )
        db.commit()

    finally:
        cursor.close()
        db.close()

    return redirect("/todos")


@app.route("/edit/<int:todo_id>", methods=["POST"])
def edit_task(todo_id):
    if "user_id" not in session:
        return redirect("/login")

    title = request.form.get("title", "").strip()

    if not title:
        return "Title is required", 400

    if len(title) > 200:
        return "Title is too long", 400

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            """UPDATE todos
               SET title = %s
               WHERE todos_ID = %s AND user_ID = %s""",
            (title, todo_id, session["user_id"])
        )
        db.commit()

    finally:
        cursor.close()
        db.close()

    return redirect("/todos")


@app.route("/done/<int:todo_id>", methods=["POST"])
def mark_done(todo_id):
    if "user_id" not in session:
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            """UPDATE todos
               SET is_done = 1
               WHERE todoS_ID = %s AND user_ID= %s""",
            (todo_id, session["user_id"])
        )
        db.commit()

    finally:
        cursor.close()
        db.close()

    return redirect("/todos")


@app.route("/not-done/<int:todo_id>", methods=["POST"])
def mark_not_done(todo_id):
    if "user_id" not in session:
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            """UPDATE todos
               SET is_done = 0
               WHERE todoS_ID = %s AND user_ID = %s""",
            (todo_id, session["user_id"])
        )
        db.commit()

    finally:
        cursor.close()
        db.close()

    return redirect("/todos")


@app.route("/delete/<int:todo_id>", methods=["POST"])
def delete_task(todo_id):
    if "user_id" not in session:
        return redirect("/login")

    db = get_db_connection()
    cursor = db.cursor()

    try:
        cursor.execute(
            """DELETE FROM todos
               WHERE todos_ID = %s AND user_id = %s""",
            (todo_id, session["user_id"])
        )
        db.commit()

    finally:
        cursor.close()
        db.close()

    return redirect("/todos")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)