from website import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(username):
    return User.query.get(str(username))

class User(db.Model, UserMixin):
    username = db.Column(db.String(35), primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def get_id(self):
        return str(self.username)

    def __repr__(self):
        return f"User(username={self.username!r}, email={self.email!r}, password={self.password!r})"

# WARNING: Make sure you change this when you officially set up the databases to avoid
# errors or wiping the data.
db.create_all()
