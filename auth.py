from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine. setProperty("rate", 138)
    engine.say(text)
    engine.runAndWait()

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()


        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                speak('Logged in successfully!')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
                speak('Incorrect password, try again.')
        else:
            flash('Email does not exist.', category='error')
            speak('Email does not exist.')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
            speak('Email already exists')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
            speak('Email must be greater than 3 characters')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
            speak('Passwords don\'t match.')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
            speak('Password must be at least 7 characters.')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            flash('Account created')
            return redirect(url_for('views.home'))
    
    return render_template("sign_up.html", user=current_user)
    
        


@auth.route('/Chatbot', methods=['GET', 'POST'])
def chatbot():
       

    return render_template("sign_up.html", user=current_user)
