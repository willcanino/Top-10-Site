from website.db_models import User
import flask_wtf
import wtforms, wtforms.validators as validators

# Lol it took me forever to figure out how to get this value 🙄
max_length_username = User.__table__.c.username.type.length
class RegistrationForm(flask_wtf.FlaskForm):
    username = wtforms.StringField('Username',
                                    validators=[validators.DataRequired(), validators.Length(min=4, max=max_length_username)])
    email = wtforms.StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = wtforms.PasswordField('Password', validators=[validators.DataRequired()])
    confirm_password = wtforms.PasswordField('Confirm Password',
                        validators=[validators.DataRequired(), validators.EqualTo('password')])

    submit = wtforms.SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(flask_wtf.FlaskForm):
    email = wtforms.StringField('Email', validators=[validators.DataRequired(), validators.Email()])
    password = wtforms.PasswordField('Password', validators=[validators.DataRequired()])
    submit = wtforms.SubmitField('Login')
