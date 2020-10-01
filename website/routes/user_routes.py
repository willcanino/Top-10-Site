from flask import redirect, flash, render_template, url_for
from flask_login import login_user, current_user, logout_user, login_required
from website.forms import LoginForm, RegistrationForm
from website import app, db, bcrypt
from website.db_models import User

@app.route('/sign-up', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect('home')
    registration_form = RegistrationForm()
    if registration_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('UTF-8')
        new_user = User(username=form.username.data,
                        email=form.email.data,
                        password=hashed_password)
        db.session.add(user); db.session.commit()
        return redirect(url_for('login'))
    return render_template('sign-up-page.html', form=registration_form)
