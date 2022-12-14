from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iszlc-sqlite3.db'
app.config['SECRET_KEY'] = '51883dce7428e2abbf7843b6'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
login_manager.login_message = u"Zaloguj się, aby uzyskać dostęp do tej strony"

from iszlc import routes