import os
import requests

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from flask_socketio import SocketIO, emit
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from modules.helpers import apology, login_required

# Configure application
app = Flask(__name__)
# app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
socketio = SocketIO(app)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///weconverse.db")


@app.route("/")
@login_required
def index():
    return render_template("index.html", initial=session["name"][0].capitalize())


@app.route("/login", methods = ["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    if request.method ==  "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]['hash'], password):
            return apology("Invalid username or password", 403)

        # Remember which user has logged in and user's name
        session["user_id"] = rows[0]["id"]
        session["name"] = rows[0]["name"]

        return redirect("/")

    return render_template("login.html")


@app.route("/sign-up", methods = ["GET", "POST"])
def sign_up():
    """Sign user up"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":

        # Store the password entered by the user
        password = request.form.get("password")

        # Ensure the confiramtion password matches the first password
        if password != request.form.get("confirmation"):
            return apology("Sorry your passwords don't match", 403)

        # Ensure password is at least 8 characters long and contains at least one number
        elif len(password) < 8:
            return apology("Sorry, your password must be at least 8 characters long and contain a number", 403)

        # Ensure the password contains at least one number
        else:
            flag = False

            # Iterate over all the character in the password checking to see if there a number
            for i in range(len(password)):
                try:
                    charPassword = int(password[i])
                    flag = True
                    break
                except:
                    continue

            # Ensure the was at least one number before proceeding
            if not flag:
                return apology("Sorry, your password must contain at least one number", 403)

        # Add a middle name to the name variable if there is any otherwise just the
        # first and last name
        if not request.form.get("middlename"):
            name = request.form.get("firstname") + ' ' + request.form.get("lastname")
        else:
            name = request.form.get("firstname") + ' ' + request.form.get("middlename") + ' ' + request.form.get("lastname")

        username = request.form.get("username")

        # Hash password before inserting it into the database
        db.execute("INSERT INTO users(name, username, hash) VALUES(?, ?, ?)", name, username,
            generate_password_hash(password))

        # Get the current username registered with in order to attach a cookie to it
        rows = db.execute("SELECT id FROM users WHERE username = ?", username)

        # Remember which user has logged in and user's name
        session["user_id"] = rows[0]["id"]
        session["name"] = rows[0]["name"]

        # Redirect user to homepage
        return redirect("/")

    return render_template("sign-up.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


@app.route("/friends")
def friends():
    return render_template("friends.html")


@app.route("/settings")
def settings():
    return render_template("settings.html")


# @app.route("/history")
# @login_required
# def history():
#     return render_template("history.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)