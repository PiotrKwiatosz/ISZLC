from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, 
             static_url_path='',
             static_folder='/static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///iszlc.db'
db = SQLAlchemy(app)

from iszlc import routes