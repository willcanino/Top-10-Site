from flask import Flask
from dotenv import dotenv_values

# Load environment variables
# Flask will autoload variables from .env file when using
# `flask run` command or running the `app.py` file
app = Flask(__name__)
app.config.from_mapping(**dotenv_values())

# Weird circular imports going on here
# but we must import routes **AFTER** we create
# the app variable or else there will be a variable
# not found error
from website import routes
