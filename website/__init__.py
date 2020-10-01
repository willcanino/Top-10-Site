from flask import Flask
from flask_mail import Mail
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import dotenv_values

# Load environment variables
# Flask will autoload variables from .env file when using
# `flask run` command or running the `app.py` file
app = Flask(__name__)
config_dict = dotenv_values()
del config_dict['contact_page_email']
if 'SQLALCHEMY_ECHO' in config_dict:
    config_dict['SQLALCHEMY_ECHO'] = config_dict['SQLALCHEMY_ECHO'] == 'True'
app.config.from_mapping(**config_dict)

mail = Mail(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

# Weird circular imports going on here
# but we must import routes **AFTER** we create
# the app variable or else there will be a variable
# not found error
from website import routes
