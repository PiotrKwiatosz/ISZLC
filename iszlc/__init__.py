from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iszlc.db'
app.config['SECRET_KEY'] = 'gsdget32536ywshsdyw3d'
db = SQLAlchemy(app)


from iszlc import routes