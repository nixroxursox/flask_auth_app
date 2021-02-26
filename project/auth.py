# auth.py
from flask import Flask
from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
    g,
    session,
)
from flask_login import login_user, logout_user, login_required
import nacl.pwhash
import functools


auth = Blueprint("auth", __name__)


@auth.route("/login")
def login():
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    name = request.form.get("name")
    password = request.form.get("password")
    PIN = request.form.get("PIN")
    remember = True if request.form.get("remember") else False

    user = User.query.filter_by(name=name).first()

    # chzeck if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    # if not user or not check_password_hash(user.password, password):
    if not user or not nacl.pwhash.argon2id.str.verify(user.password, password):
        flash("Please check your login details and try again.")
        return redirect(
            url_for("auth.login")
        )  # if user doesn't exist or password is wrong, reload the page

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for("main.profile"))


@auth.route("/signup")
def signup():
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():

    name = request.form.get("name")
    password = request.form.get("password")
    PIN = request.form.get("PIN")

    user = User.query.filter_by(
        name=name
    ).first()  # if this returns a user, then the email already exists

    if user:  # if a user is found, we want to redirect back to signup page so user
        flash("Username already exists")
        return redirect(url_for("auth.signup"))

    # create new user with the form data. Hash the password so plaintext versio
    new_user = User(
        name=name,
        password=nacl.pwhash.argon2id.str(password),
        PIN=nacl.pwhash.argon2id.str(PIN),
    )

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for("auth.login"))


@auth.route("/register", methods=("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["name"]
        password = request.form["password"]
        PIN = request.form["PIN"]
        db = get_db()
        error = None

        if not name:
            error = "Username is required."
        elif not password:
            error = "Password is required."
        elif (
            db.execute("SELECT id FROM Users WHERE name = ?", (name,)).fetchone()
            is not None
        ):
            error = "User {} is already registered.".format(name)

        if error is None:
            db.execute(
                "INSERT INTO Users (name, password) VALUES (?, ?)",
                (username, generate_password_hash(password)),
            )
            db.commit()
            return redirect(url_for("auth.login"))

        flash(error)

    return render_template("auth/register.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
