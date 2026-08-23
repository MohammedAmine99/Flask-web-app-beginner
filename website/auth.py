from flask import Blueprint, render_template , request, flash , redirect , url_for
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash




auth = Blueprint('auth', __name__)

@auth.route('/home')
def home():
    return render_template("home.html")

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True, text="This is the login page", user="John Doe")

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        passwordConfirm = request.form.get('passwordConfirm')

        if len(email) < 4:
            flash('Email must be greather than  4 characters.', category='error')
        elif len(firstName) < 2:
            flash('First name must be greather than 2 characters.', category='error')
        elif len(lastName) < 2:
            flash('Last name must be greather than 2 characters.', category='error')
        elif password != passwordConfirm:
            flash('Passwords do not match.', category='error')
        elif len(password) < 7:
            flash('Password must be at least 7 characters long.', category='error')
        else:
            new_user = User(email=email, first_name=firstName, last_name=lastName, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully!', category='success')
            return redirect(url_for('views.home'))
            #add user to database

    return render_template("sign_up.html")