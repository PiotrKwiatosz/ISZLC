from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iszlc.db'
app.config['SECRET_KEY'] = '51883dce7428e2abbf7843b6'
db = SQLAlchemy(app)

from iszlc import routes