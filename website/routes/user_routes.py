from flask import redirect, flash, render_template, url_for
from flask_login import login_user, current_user, logout_user, login_required
from website.forms import LoginForm, RegistrationForm
from website import app, db, bcrypt
from website.db_models import User

@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(registration_form.password.data).decode('UTF-8')
        new_user = User(username=registration_form.username.data,
                        email=registration_form.email.data,
                        password=hashed_password)
        db.session.add(new_user); db.session.commit()
        return redirect(url_for('login'))
    return render_template('sign-up-page.html', form=registration_form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.get(login_form.email_or_username.data) or \
                User.query.filter_by(email=login_form.email_or_username.data).first()
        if user and bcrypt.check_password_hash(user.password, login_form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        flash('Login failed. Please check your username/email and password.')
    return render_template('login-page.html', form=login_form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))
